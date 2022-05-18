'''
Created on Apr 21, 2016

@author: nconnors
'''

from vocollect_core.utilities import class_factory, obj_factory
from LUT.voice_attribute_error import VoiceAttributeError
from mlSharedConstants import NAME, VALUE, \
    MLPROCESSOR_TASK_NAME, RLMENU_TASK_NAME, GOTO_MAIN_MENU, JUMEX_TCODE_TASK_BASE_NAME
#from tcodes.rlmenu import GOTO_MAIN_MENU
from processor.processor import POST_INIT
from vocollect_core.dialog.functions import prompt_ready
from vocollect_core.utilities.localization import itext
from voice import log_message
from vocollect_core.dialog.base_dialog import BaseDialog
from tcodes.tcodeTaskBase import TcodeTaskBase


OPTION  = 'option'

#============================================================
# tcode task base used and is extended by all tcode tasks
#============================================================
class jumex_TcodeTaskBase(class_factory.get(TcodeTaskBase)):
    
    #----------------------------------------------------------
    def __init__(self, tcd, taskRunner = None, callingTask = None):
        
        super(jumex_TcodeTaskBase, self).__init__(tcd, taskRunner, callingTask)

        #Set task name
        self.name = JUMEX_TCODE_TASK_BASE_NAME
        
        
    #----------------------------------------------------------
    def post(self):
        ''' post the command to the PT.  NOTE: that ALL posts to the PT are handled by this method '''
        self._what_to_speak = ''
        try:
            self.tcd._lut.post(self.tcd._command, self.tcd._name_value_pairs)
        except VoiceAttributeError as err: #@UnusedVariable
            ''' We failed to build a valid instruction set.  This typically means that something went
            wrong in the build_instructions method of the VDERP Lut class.  Our only option is to 
            send the user back to the Welcome Prompt. '''
            # notify user of error
            prompt_ready(itext('error.login.problem'), priority_prompt=True)
            # force sign off to get back to sign on
            self.post_sign_off()
            return
        except Exception as err: #@UnusedVariable
            ''' In all cases retry the post. 
                If we modify our application to send a transaction ID and we modify the service handler 
                on the SAP side to take advantage of this, we could potentially deal with this issue to avoid 
                duplicate posts.   ''' 
            self.tcd._posting_error_detected = True
            
            # notify operator of timeout error indicating that they should use 'report problem'
            # and will then be returned to the main menu
            BaseDialog.exclude_dynamic_vocab = True
            prompt_ready(itext('tcd.posting.timeout.error.message'))
        
            self.mainMenu()
            return

        ''' We got a valid response and instruction back from the host... process it 
        save the command and name/value pairs for processing below in the case of a 
        RePost command from an error screen. '''
        self.tcd.posting_error_detected = False
       
        # initialize values for new screen
        self.tcd._previous_command = self.tcd._command
        self.tcd._previous_name_value_pairs = self.tcd._name_value_pairs
        self.tcd._current_instruction_set = self.tcd._lut.get_instructions
        self.tcd._lut_help_messages = self.tcd._lut.get_help_messages
        self.tcd._name_value_pairs = {}
        # set current and previous screen values
        self.tcd._previous_screen = self.tcd._current_screen
        self.tcd._current_screen = self.tcd._current_instruction_set._screen_id

        ''' retrieve the screen values and put them in the local variables '''
        self.tcd.v = {}
        
        for instruction in self.tcd._current_instruction_set._list:
            self.tcd.v[instruction.fieldid] = {NAME:instruction.fieldname, 
                                           VALUE:instruction.fieldvalue}
        
        # if screen is a PT error screen then process it here
        if 'PT-ERROR' in self.tcd._current_screen:
            if 'PT-ERROR' in self.tcd._previous_screen:
                # this indicates that a PT error was processed and sign off
                # posted to PT.  Now restart with new session 
                self.return_to(MLPROCESSOR_TASK_NAME, POST_INIT)
            else:
                self.processPtError()        
        
    #----------------------------------------------------------
    def signOff(self):
        # confirm sign off
        # log out automatically
        self.buildNameValuePairs('/NEX')
        self.next_state = ''
        self.tcd._isStartup = True
        self.tcd._command = "SignOff"
        self.tcd.signOffRequest = False
        self.post()
        self.return_to(MLPROCESSOR_TASK_NAME, POST_INIT)
                
    #----------------------------------------------------------
    def mainMenu(self, calledFromMenu = False):
        ''' determines current screen value and calls mainMenu with back
            button value to get to a menu screen.  If the current screen is
            nested below the top screen for the tcode it may be necessary to 
            post 'back' more than once before getting to a menu screen.
            After a menu screen is reached (contains 'RLMENU' in its name)
            Input parameter screens is a dictionary with screen names for keys
            and button values for values 
             '''
        
        # counter to insure that we don't end up in an endless loop should the
        # use of the 'back' button not result in reaching a menu screen.  This 
        # could potentially happen if posting 'back' (or its equivalent) for a 
        # screen does not result in a different screen being sent from SAP.
        screenDepth = 0
        screenDepthLimit = 10
        
        while(True):
            if 'SAPLRF_SSCR0011' in self.tcd._current_screen.upper():
                # if this was called from main menu then we are trying to recover
                # from an out of synch situation.  RLMENU is the current tocde
                # so just return when a menu screen is found.  
                if calledFromMenu == True:
                    return
                # we are at a menu screen - OK to return to RLMENU task
                # and go to main menu
                self.tcd._tcode = 'MENU'
                self.next_state = ''
                self.return_to(RLMENU_TASK_NAME, GOTO_MAIN_MENU)
            elif self.tcd._current_screen.upper() in self.tcd.tcodeScreens.keys():
                self.buildNameValuePairs(self.tcd.tcodeScreens[self.tcd._current_screen])
                self.post()
            elif calledFromMenu == True:
                # if trying to get back to main menu from the menu tcode try finding value
                # for back button.  If not found then try using enter = '/0'.
                # The screen depth functionality should stop this attempt if it fails
                self.buildNameValuePairs(self.findBackButton())
                self.post()
            else:
                # If the screen is not in the list then log an error message, speak error message
                # and log operator off.
                log_message('ERROR: unexpected screen seen when navigating to menu from inside tcode' + \
                            ' ' + self.tcd._tcode + ', screen ' + self.tcd._current_screen)
                self.signOff()

            screenDepth = screenDepth + 1
            if screenDepth > screenDepthLimit:
                # this is our escape path from this loop.  If a tcode is
                # with a depth greater than 10 then screenDepthLimit needs
                # to be increased.
                log_message('ERROR: screen depth limit reached while navigating to main menu from inside tcode' + \
                            ' ' + self.tcd._tcode + ', last screen when navigating to main menu was ' + self.tcd._current_screen + \
                            ', with screen depth at error = ' + str(screenDepth))
                log_message('tcode screens = ' + str(self.tcd.tcodeScreens))
                prompt_ready(itext('tcd.posting.timeout.error.with.signoff'))
                self.signOff()
        
    #----------------------------------------------------------
    def processPtError(self):
        ''' process error messages returned from the PT '''
        
        if self.tcd._current_screen == 'PT-ERROR-1523':
            # check for a session timeout.  This response can be returned as a response 
            # to any post since the operator can take too long to respond to any prompt.
            # Error message from PT: Session timed out. Please sign on.  To continue say ready.
            prompt_ready(itext('error.session.timed.out'))
            # do not sign off when timeout occurs
            return
        elif self.tcd._current_screen == 'PT-ERROR-1521':
            # this screen is being returned from the PT when login fails   
            prompt_ready(itext('error.login.problem'))
        elif self.tcd._current_screen == 'PT-ERROR-1522':
            # this screen is being returned from the PT when the voice attribute
            # file is not found for the unknown popup screen that appears
            # periodically when posting a pick            
            prompt_ready(itext('error.posting.continue.message'))       
        elif self.tcd._current_screen == 'PT-ERROR-1544':
            # this screen is being returned from the PT when a post to SAP fails
            prompt_ready(itext('error.posting.continue.message'))       
        elif self.tcd._current_screen == 'PT-ERROR-1551':
            # this screen is being returned from the PT when the number of login attempts exceeds 
            # permitted # of attempts
            prompt_ready(itext('error.exceed.attempts.message'))       
        else:  # default PT error message
            # include PT error #    
            # don't speak bogus error message if current screen is SAPLRSRC_DYNPRO0001
            if self.tcd._current_screen != 'SAPLRSRC_DYNPRO0001':       
                prompt_ready(itext('error.default.error.message', 
                               self.tcd._current_screen.split('-')[2]))             

        # always sign off when a PT error is received
        self.signOff()
        
    #--------------------------------------------------------------------------
        
# This line of code replaces the TcodeTaskBase class with the customization version
obj_factory.set_override(TcodeTaskBase, jumex_TcodeTaskBase)
