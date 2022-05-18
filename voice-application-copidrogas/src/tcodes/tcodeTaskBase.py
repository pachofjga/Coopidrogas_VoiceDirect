'''
Created on Apr 21, 2016

@author: nconnors
'''

from vocollect_core.utilities import class_factory
from vocollect_core.task.task import TaskBase
from LUT.voice_attribute_error import VoiceAttributeError
from mlSharedConstants import TCODE_TASK_BASE_NAME, NAME, VALUE, \
    MLPROCESSOR_TASK_NAME, RLMENU_TASK_NAME, RETURN_TCODE, AUTO_RUN_TCODE,\
    AUTO_RUN_START, AUTO_RUN_STATE
#from tcodes.rlmenu import GOTO_MAIN_MENU
from processor.processor import POST_INIT, POST_TO_HOST, POST_SIGNOFF
from vocollect_core.dialog.functions import prompt_ready, prompt_digits,\
    prompt_only
import random
from vocollect_core.utilities.localization import itext
import re
from voice import log_message, get_voice_application_property
from vocollect_core.scanning import ScanMode
from vocollect_core.dialog.base_dialog import BaseDialog


OPTION  = 'option'
GOTO_MAIN_MENU = 'gotoMainMenu'

#============================================================
# tcode task base used and is extended by all tcode tasks
#============================================================
class TcodeTaskBase(class_factory.get(TaskBase)):
    
    #----------------------------------------------------------
    def __init__(self, tcd, taskRunner = None, callingTask = None):
        
        super(TcodeTaskBase, self).__init__(taskRunner, callingTask)

        #Set task name
        self.name = TCODE_TASK_BASE_NAME
        
        self._regex = None

        # set local _data variable to parameter value
        self.tcd = tcd
        
        # initialize current and previous screens
        self.tcd._current_screen = self.tcd._current_instruction_set.screen_id
        self.tcd._previous_screen = ''
        
        # posts from tcode tasks will have a command of 'Post'
        # Change this value if different value is needed.
        self.tcd._command = 'Post'
        
        for instruction in self.tcd._current_instruction_set._list:
            self.tcd.v[instruction.fieldid] = {NAME:instruction.fieldname, 
                                           VALUE:instruction.fieldvalue}
        
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
            
            # This is breaking the rule of trying to keep tcodeTaskBase generic
            # This could be considered a customization for Groveport that would not
            # be in the core VDERP product.  I suppose we would override this method
            # for Groveport.  We need to treat this screen special because it has
            # no buttons to use for exiting it.  The only way that the tcode
            # supports exiting it is to successfully enter all the requested SN's
            # and then send the 'save' button.  
            # Special handling for serial number screen timeouts. There is no way to navigate to 
            # the main menu because the screen doesn't have buttons to exit without completing 
            # entry of all serial numbers.  Therefore, the operator will be forced to sign off
            # if a communications timeout is detected while on the serial number screen.  
            if self.tcd._current_screen == 'ZRPLO_PICKPACK_RF_1SCR_V300':
                # provide special timeout error notification indicating that the operator
                # will be signed off due to communications timeout error.
                BaseDialog.exclude_dynamic_vocab = True
                prompt_ready(itext('tcd.posting.timeout.error.with.signoff'))
                self.signOff()
                return
                
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
        self.tcd._previous_instruction_set = self.tcd._current_instruction_set
        self.tcd._current_instruction_set = self.tcd._lut.get_instructions
        self.tcd._lut_help_messages = self.tcd._lut.get_help_messages
        self.tcd._name_value_pairs = {}
        # set current and previous screen values
        self.tcd._previous_screen = self.tcd._current_screen
        self.tcd._current_screen = self.tcd._current_instruction_set._screen_id

        # save the variables from the previous screen
        self.tcd.previous_v = self.tcd.v
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
        self.post()
        self.return_to(MLPROCESSOR_TASK_NAME, POST_INIT)
                
    #----------------------------------------------------------
    def getMessage(self):
        ''' method to retrieve contents of message screen and return it '''
        
        message = ''
        
        for instruction in self.tcd._current_instruction_set._list:
            if instruction._command == 'SpeakPrompt':
                message = message + instruction.fieldvalue + ' '
        return message
            
    #----------------------------------------------------------
    def getCheckDigitGroup(self, currentGroup):
        ''' There are 3 available check digit group positions.  This method returns 
            a random check digit group position. If the currentGroup parameter is an
            empty string then the returned group will be one of the 3 group positions.
            If the currentGroup parameter is one of 'left', 'middle' or 'right' then
            the randomized group position returned will be one of the other positions. '''
        
        # valid positions
        positions = ['left', 'middle', 'right']
        position_keys = ['sgp.left.position', 'sgp.middle.position', 'sgp.right.position']
        
        if len(currentGroup) != 0:
            positions.remove(currentGroup)
        
        newGroup = random.choice(positions)
        
        localizedNewGroup = position_keys[positions.index(newGroup)]
            
        return itext(localizedNewGroup)
            
    #----------------------------------------------------------
    def buildNameValuePairs(self, okCodeValue):
        ''' populates name/value pairs with current values '''
        
        # insure that dictionary is empty at start
        self.tcd._name_value_pairs = {}
        
        for fieldID in self.tcd.v:
            if self.tcd.v[fieldID][NAME] != '~OKCode':
                # only save values other than buttons that will have a name of '~OKCode'                
                self.tcd._name_value_pairs[self.tcd.v[fieldID][NAME]] = \
                    self.fixURL(self.tcd.v[fieldID][VALUE])
            
        # the desired value for the ~OkCode for this screen   
        self.tcd._name_value_pairs['~OkCode'] = okCodeValue

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
        
        # counter to insure that we don't en up in an endless loop should the
        # use of the 'back' button not result in reaching a menu screen.  This 
        # could potentially happen if posting 'back' (or its equivalent) for a 
        # screen does not result in a different screen being sent from SAP.
        screenDepth = 0
        screenDepthLimit = 10
        
        while(True):
            if 'RLMENU' in self.tcd._current_screen.upper():
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
        else:  # default PT error message
            # include PT error #            
            prompt_ready(itext('error.default.error.message', 
                               self.tcd._current_screen.split('-')[2]))             

        # always sign off when a PT error is received
        self.signOff()
        
    #----------------------------------------------------------
    def fixURL(self, strVal):
        ''' Data being returned to SAP may have characters that the PT
            cannot include in the URL data.  These include: #, :, =, &, !, ?, ',', and others
            This method will strip out the listed values.  If/when others are encountered
            they should be added to this list. '''
        
        if self._regex == None:
            self._regex = re.compile('[:\$#@!&+=%?,]')
             
        return self._regex.sub(' ', strVal)
    
    #----------------------------------------------------------
    def restartTcode(self):
        ''' permits a tcode to restart at its entry point from the
            voice menu by reposting its option on the SAP menu to
            restart itself.  Note that this does not check to insure
            that the menu with the tcode option is currently displayed.
            It is the responsibility of the implementer to either check
            at runtime or be certain that the SAP flow logic will insure
            that the menu is displayed such as is seen when 'back' is 
            used or the tcode completes.   '''
        
        # initialize auto run values:
        self.tcd._autoRun[RETURN_TCODE] = ''
        self.tcd._autoRun[AUTO_RUN_TCODE] = self.tcd._tcode
        self.tcd._autoRun[AUTO_RUN_STATE] = AUTO_RUN_START
        
        # return to main menu and let main menu handle
        # autorun flow
        self.mainMenu()

    #--------------------------------------------------------------------------
    def findBackButton(self):
        ''' used when trying to recover from an out of synch condition.
            This method looks through the current instruction set list for the
            current screen trying to find the word 'BACK'.  If found, then
            the button value is returned.  If not found then the value for 
            enter ('/0') is returned. '''
            
        for element in self.tcd._current_instruction_set._list:
            if element.command == 'Button':
                if 'BACK' in element.fieldid.upper()  or \
                        'BCK' in element.fieldid.upper() or \
                        'BACK' in element.fielddescription.upper() or \
                        'BCK' in element.fielddescription.upper() or \
                        'BACK' in element.fieldvalue.upper() or \
                        'BCK' in element.fieldvalue.upper():
                    return element.fieldvalue
            
        return '/0'

    #----------------------------------------------------------
    def getValue(self,fieldName):
        ''' checks to insure that variable exists and if it does returns the value,
            otherwise returns an empty string '''
        
        if fieldName in self.tcd.v:
            return self.tcd.v[fieldName][VALUE]
        
        return ''
        
    #----------------------------------------------------------
    def setValue(self,fieldName, value):
        ''' checks to insure that variable exists and if it does sets the value,
            no error condition is returned if it doesn't exist.  This is functionality
            designed to avoid an exception that will result in a task error because the 
            variable doesn't exist.  Error handling functionality is the responsibility 
            of the calling method '''
        
        if fieldName in self.tcd.v:
            self.tcd.v[fieldName][VALUE] = value
        
    #--------------------------------------------------------------------------
    def exists(self,fieldName):
        ''' checks to see if the specified field exists in the data received from SAP '''
        
        if fieldName in self.tcd.v:
            return True
        return False
            
    #--------------------------------------------------------------------------
    def usePreviousScreen(self):
        ''' resets the instruction set and posting variables to those for the previous
            screen.  This functionality is used when a screen is returned with an embedded
            error message.  The message needs to be processed however there are no buttons
            on the screen to post it to SAP.  SAP expects the previously received screen data
            without the message to be posted.  '''
        
        self.tcd._current_instruction_set = self.tcd._previous_instruction_set
        self.tcd.v = self.tcd.previous_v
        
    #--------------------------------------------------------------------------
        
        