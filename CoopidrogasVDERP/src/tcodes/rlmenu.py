'''
Created on Apr 20, 2016

@author: nconnors
'''
from vocollect_core.utilities import class_factory, obj_factory

from mlSharedConstants import RLMENU_TASK_NAME, AUTO_RUN_STATE, \
    RETURN_TCODE, AUTO_RUN_TCODE, AUTO_RUN_NOT_ACTIVE, AUTO_RUN_START, AUTO_RUN_RETURN

from tcodes.tcodeTaskBase import TcodeTaskBase
from vocollect_core.dialog.functions import prompt_ready, prompt_list
from vocollect_core.utilities.localization import itext
import voice

#from tcodes import * #@UnusedWildImport
from voice import log_message

# state definitions
GOTO_MAIN_MENU          = 'gotoMainMenu'
SELECT_TCODE            = 'selectTcode'
GOTO_TCODE_MENU         = 'gotoTcodeMenu'
RUN_TCODE               = 'runTcode'

OPTION  = 'option'
TEXT    = 'text'

#===========================================================
# tcode RLMenu task used to process SAP menus
#===========================================================
class RLMenu(class_factory.get(TcodeTaskBase)):
    
    #----------------------------------------------------------
    def __init__(self, tcd, taskRunner = None, callingTask = None):
        
        super(RLMenu, self).__init__(tcd, taskRunner, callingTask)

        # Set task name
        self.name = RLMENU_TASK_NAME
        
        # ************************************************************************
        # ADD TCODES HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # ************************************************************************
        # list of tcode tasks
        # TDOD: come up with a way to instantiate tcode tasks dynamically
        # to avoid the need to add them here.  They are already being imported
        # dynamically by placing them in the __all__ list for the tcode package.
        # Currently each tcode must be manually added to this list and the
        # __all__ list in tcodes.__init__ 
        # Enter values in tcodeList using format <file name>.<class name>
        self.tcodeList = []
        
        # Initialize the main menu identifier using the first entry for any 
        # one of the tcodes in the SAP menu dictionary.  All tcodes must 
        # start on the same main menu so the option:text values for sequence
        # 1 of any one of the tcodes will identify the main menu.
        self._main_menu = {}
        self._main_menu[OPTION] = 'TEXT' + str(self.tcd._sapMenu[self.tcd._voiceMenu[1]][1][OPTION])
        self._main_menu[TEXT] = self.tcd._sapMenu[self.tcd._voiceMenu[1]][1][TEXT]
             
        # voice menu containing a list of menu #'s and identifying menu text
        self._voiceMenuOptions = []
        index = 1
        while index <= len(self.tcd._voiceMenu):
            option = [str(index), itext(self.tcd._voiceMenu[index])]
            self._voiceMenuOptions.append(option)
            index = index + 1    
                
        # menu screen names - needs to contain all menu screen names that might be seen
        # by menu tcode.  Since Helsby site already uses RLMEU888-1 and rlmenu we need
        # to be able to accept both of those names as screen names for menus.
        self._menu_screen_names = ['RLMENU888-1','rlmenu_888', 'RLMENU_888']
        
        self.resynchToMainMenu = False



    #----------------------------------------------------------
    def initializeStates(self):
        '''set states '''
        self.addState(GOTO_MAIN_MENU,       self.gotoMainMenu)        
        self.addState(SELECT_TCODE,         self.selectTcode)
        self.addState(GOTO_TCODE_MENU,      self.gotoTcodeMenu)     
        self.addState(RUN_TCODE,            self.runTcode)
        
    #----------------------------------------------------------
    def gotoMainMenu(self):
        ''' insures that the menu being processed is the top 
            menu.  If the menu option text defined for the 
            top menu does not match the menu option text for 
            the current menu then the back button will be
            returned to SAP.  This should result in the next
            higher level menu being returned from SAP.  This
            process will continue until the main menu is reached. '''
        
        try:
            # check for non-menu screen
            log_message('GO_TO_MAIN_MENU state: screen is ' + self.tcd._current_screen)

            if 'RLMENU' not in self.tcd._current_screen.upper():
                prompt_ready(itext('error.unexpected.signing.off.message'))

                self.signOff()
            
            elif self.tcd._current_instruction_set._dict[self._main_menu[OPTION]].fielddescription \
                    != self._main_menu[TEXT]:
                # indicates we are not at the main menu
                # post back button
                self.postBackButton()
                self.next_state = self.current_state
                return
            
        except KeyError as err: #@UnusedVariable
            # This error occurs when the current menu from SAP does not have
            # an entry for the option associated with the index that we are
            # looking for to identify the main screen.  
            # For instance, if the option value for main menu is 6 but the
            # current menu returned by SAP only has 2 options then a comparison
            # of the 6th entry in the current SAP menu will fail with a key 
            # error because there is no 6th entry in that menu.  This indicates 
            # that the current menu screen is not the main menu screen, 
            # therefore simply post the back button to go to the next higher
            # up screen.
            
            # a special case can occur if the SAP session is on the get serial
            # number screen.  There is no back button so using the back button
            # to exit out of the tcode screen won't work here like with the
            # other tcodes.  The only way to get out of the serial number screen
            # is to sign off.  To handle this case we will check for the serial
            # number screen and if detected will sign off
            if self.tcd._current_screen == 'ZRPLO_PICKPACK_RF_1SCR_V300':
                self.signOff()
            else:
                self.postBackButton()
                self.next_state = self.current_state
                return
            
        # check to see if this state is being used to resynch to the main menu
        # If so, then skip the SELECT_TCODE state and proceed to tcode
        if self.resynchToMainMenu == True:
            log_message('GO_TO_MAIN_MENU state: resynch complete so skip SELECT_TCODE state')
            self.resynchToMainMenu = False
            # include a final check to make sure that the tcode is not still
            # set to the menu.  If so then just proceed with tcode selection
            if self.tcd._tcode != 'MENU':
                self.next_state = GOTO_TCODE_MENU
                
        # otherwise we are at the top menu so proceed to select tcode

    #----------------------------------------------------------
    def selectTcode(self):
        ''' selectTcode gets the operator response to the voice menu 
            and posts it to SAP '''
        
        # check self._autoRun to see if we need to process an auto run
        # request
        if self.tcd._autoRun[AUTO_RUN_STATE] == AUTO_RUN_NOT_ACTIVE:
        
            # prompt operator for selection
            menu_selection = prompt_list(self._voiceMenuOptions,
                                 itext('rlm.function.prompt'),
                                 itext('rlm.function.number.message'),
                                 {'sign off':True})
    
            if menu_selection == 'sign off':
                # tcode: sign off
                self.signOff()
                return
            else:
                # we should have a valid selection
                self.tcd._tcode = self.tcd._voiceMenu[int(menu_selection)]

        elif self.tcd._autoRun[AUTO_RUN_STATE] == AUTO_RUN_START:
            # starting the auto run process by executing the AUTO_RUN_TCODE tcode
            self.tcd._tcode = self.tcd._autoRun[AUTO_RUN_TCODE]

        elif self.tcd._autoRun[AUTO_RUN_STATE] == AUTO_RUN_RETURN:
            # check to see if auto run has a return tcode
            if self.tcd._autoRun[RETURN_TCODE] != '':
                # completing the auto run process by executing the AUTO_RUN_TCODE tcode
                self.tcd._tcode = self.tcd._autoRun[RETURN_TCODE]
            else:
                # this indicates that the auto run functionality was used to automatically
                # launch a tcode but no return tcode was specified.  Therefore, simply
                # mark the auto run functionality as complete and re-execute this state
                # to prompt the operator for the next tcode
                self.tcd._autoRun[AUTO_RUN_STATE] = AUTO_RUN_NOT_ACTIVE
                self.next_state = self.current_state

    #----------------------------------------------------------
    def gotoTcodeMenu(self):
        ''' processes menus until the menu with the tcode is found
            at which point flow goes to the execute tcode state '''
        
        # determine which of the menus for the tcode is currently displayed
        index = len(self.tcd._sapMenu[self.tcd._tcode])
        while index > 0:
            # we start with the highest index since it is the tcode menu.
            # We should always be at the main menu when this state is
            # first executed following the tcode selection in SELECT_TCODE
            # since that is the job of the GOTO_MAIN_MENU state.
            # This state should be executed iteratively until we get to 
            # the tcode menu.
            try:
                if self.tcd._sapMenu[self.tcd._tcode][index][TEXT] == \
                        self.tcd._current_instruction_set._dict['TEXT' + \
                        self.tcd._sapMenu[self.tcd._tcode][index][OPTION]].fielddescription:
                    # we have a match
                    # is this the tcode menu?
                    if index != len(self.tcd._sapMenu[self.tcd._tcode]):
                        # no it is not the tcode menu therefore repeat state
                        self.next_state = self.current_state
                        log_message('GOTO_TCODE_MENU state, not at tcode menu so repeat state')
                    else:
                        log_message('GOTO_TCODE_MENU state, tcode menu found so goto RUN_TCODE state')
                    self.postMenu(index)
                    return
            except KeyError as err: #@UnusedVariable
                # This error occurs when the current menu from SAP does not have
                # an entry for the option associated with this index in the SAP menu.  
                # For instance, if the option value for SAP menu index being
                # checked is 5 but the current menu returned by SAP only has 2
                # options then a comparison of the 5th entry in the current SAP
                # menu will fail with a key error because there is no 5th entry
                # in that menu.  This indicates that this index value does not
                # match the current screen, therefore simply proceed to the next
                # index to find the index vlaue that does match this screen.
                
                # check to make sure we are still at a menu
                # When synchronization issues exist it is possible that we are not at 
                # a menu and need to try to return to the main menu before continuing.
                if 'RLMENU' not in self.tcd._current_screen.upper():
                    self.resynchToMainMenu = True
                    log_message('GOTO_TCODE_MENU state, starting menu resynch, current screen is ' + self.tcd._current_screen)
                    self.mainMenu(True)
                    self.next_state = GOTO_MAIN_MENU
                    return
            index = index - 1
        # if this code is reached then there was no match found.  This should never
        # happen unless there is a problem with the config.ini definition for this tcode
        # or the menu content has changed.  Speak a message to the operator and return 
        # to the main menu
        prompt_ready(itext('rlm.invalid.menu.path'))
        self.next_state = GOTO_MAIN_MENU
        log_message('menu path to tcode was invalid: tcode was - ' + self.tcd._tcode + \
                    ', SAP menu values: ' + str(self.tcd._sapMenu[self.tcd._tcode]))
                
    #----------------------------------------------------------
    def runTcode(self):
        ''' launches tcode task with return state set to GOTO_MAIN_MENU state '''
        
        # get tcode object
        tcode = None
        for tc in self.tcodeList:
            if self.tcd._tcode in str(tc):
                tcode = tc
                break
            
        if tcode == None:
            # TODO: add error handling here
            return
        log_message('launching tcode ' + self.tcd._tcode)
        # check to see if we are in an auto run process and adjust state as needed
        if self.tcd._autoRun[AUTO_RUN_STATE] != AUTO_RUN_NOT_ACTIVE:
            if self.tcd._autoRun[AUTO_RUN_STATE] == AUTO_RUN_START:
                # indicates that task being launched is the auto run tcode
                # change state to AUTO_RUN_RETURN
                self.tcd._autoRun[AUTO_RUN_STATE] = AUTO_RUN_RETURN
            else:
                # indicates that the tcode being launched is the return tcode
                self.tcd._autoRun[AUTO_RUN_STATE] = AUTO_RUN_NOT_ACTIVE
                
        # launch tcode task
        self.launch(obj_factory.get(tcode, self.tcd, self.taskRunner), GOTO_MAIN_MENU)

    #----------------------------------------------------------
    def postMenu(self,index):
        
        # We don't use RLMOB-MENOPT for posting menu options.  We could, however, 
        # be sharing the PT with an application that is using it and has setup 
        # voice attribute files that use the PassThrough command to automatically 
        # post menus.  Because of this possibility, always clear out this value 
        # before posting responses to menus.
        self.setValue('RLMOB-MENOPT', '')
        self.buildNameValuePairs(str(self.tcd._sapMenu[self.tcd._tcode][index][OPTION]))
        self.post()
            
    #--------------------------------------------------------------------------
    def postBackButton(self):
        ''' method to post back button to get to next higher level menu screen '''
        
        # as in postMenu() above the value of RLMOB-MENOPT must be cleared out
        if 'RLMENU' in self.tcd._current_screen.upper():
            self.setValue('RLMOB-MENOPT', '')
        self.buildNameValuePairs('/EBACK')
        self.next_state = self.current_state
        self.post()

    #--------------------------------------------------------------------------

    #=======================================================================
    # END OF STATE FUNCTIONS - the remaining functions are utility methods
    #=======================================================================


    
