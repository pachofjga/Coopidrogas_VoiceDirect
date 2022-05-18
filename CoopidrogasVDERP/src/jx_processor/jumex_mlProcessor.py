'''
Created on Aug 30, 2017

@author: nconnors
'''
from processor.processor import Processor, PROCESS_SPEAK_PROMPT, GET_DATA_STATE,\
    POST_SIGNON
from mlSharedConstants import JUMEX_MLPROCESSOR_TASK_NAME,\
    INVALID_OPERATOR_ID_FORMAT
from LUT.voice_attribute_error import VoiceAttributeError
from voice import getenv
from processor.processor import POST_TO_HOST, POST_SIGNOFF, POST_INIT,\
    PROCESS_INSTRUCTIONS
from shared_constants import LOGGED_IN
from vocollect_http.httpserver import set_display_page
from vocollect_core.utilities import obj_factory
from jx_tcodes.jumex_tcodeData import jumex_tcodeData
from voice import log_message
from vocollect_core.utilities.localization import itext
from vocollect_core.dialog.functions import prompt_ready
from tcodes.rlmenu import RLMenu
from utilities.string_helpers import insert_space

#----------------------------------------------------------
class jumex_MLProcessor(Processor):
    
    #----------------------------------------------------------
    def __init__(self, runner):
        
        # call base class init
        super(jumex_MLProcessor, self).__init__(runner)
        
        # Set task name
        self.name = JUMEX_MLPROCESSOR_TASK_NAME
                
        # initialize tcode data
        self.tcd = jumex_tcodeData()
        
    #----------------------------------------------------------
    def process_instructions(self):
        
        self._instruction = self._current_instruction_set.get_next_instruction()
        
        if  self._current_instruction_set.screen_id == '':
            self._current_instruction_set.screen_id = 'SAPLRF_SSSCR0011'
        
        if self._current_instruction_set.screen_id != 'PT-INIT-Integrated' and \
                self.tcd._current_screen != 'ENDOFSESSION':
            
            # launch tcode task for specified tcode:
            if self.tcd._tcode =='MENU' or 'RLMENU' in self._current_instruction_set.screen_id:
                if self.tcd._tcode != 'MENU':
                    log_message('tcode not MENU but current screen is ' + self._current_instruction_set.screen_id + \
                                ', forcing tcode to MENU')
                    self.tcd._isStartup = True
                else:
                    log_message('tcode = MENU')
                if self._lut._screenId.fieldid == 'PT-ERROR-1521':    # and not self.isMobileLoginForm: 
                    # this screen is being returned from the PT when logon fails   
                    # need to sign in, previous attempt to sign on failed
                    # notify user of error
                    prompt_ready(itext('error.login.problem'), priority_prompt=True)
                    # force sign off
                    # Note that the core instance of he name/value pairs will be used by 
                    # the core post not the self.tcd_name_value_pairs
                    #self._name_value_pairs['~OKCode'] = '/NEX'
                    self.tcd._isStartup = True
                    self.next_state = POST_INIT
                    return
                elif self._lut._screenId.fieldid == 'PT-ERROR-1523':    # and not self.isMobileLoginForm: 
                    # this screen is being returned from the PT when a session time out is reported   
                    # notify user of error
                    prompt_ready(itext('error.session.timed.out.problem'), priority_prompt=True)
                    # force sign off
                    # Note that the core instance of he name/value pairs will be used by 
                    # the core post not the self.tcd_name_value_pairs
                    #self._name_value_pairs['~OKCode'] = '/NEX'
                    self.tcd._isStartup = True
                    self.next_state = POST_INIT
                    return
                if self.tcd._isStartup == True:
                    # initialize tcode data to be sent to tcode task:
                    log_message('startup is True')
                    self.tcd._current_instruction_set = self._current_instruction_set
                    self.tcd._help_message = self._help_message
                    self.tcd._lut = self._lut
                    self.tcd._current_instruction_set = self._current_instruction_set
                    self.tcd._help_message = self._help_message
                    self.tcd._what_to_speak = self._what_to_speak
                    self.tcd._name_value_pairs = self._name_value_pairs
                    self.tcd._previous_name_value_pairs = self._previous_name_value_pairs
                    self.tcd._lut = self._lut
                    self.tcd._command = self._command
                    self.tcd._previous_command = self._previous_command
                    self.tcd._instruction = self._instruction
                    self.tcd._additional_vocabulary = self._additional_vocabulary
                    self.tcd._confirmation_prompts = self._confirmation_prompts
                    self.tcd._word = self._word
                    self.tcd._lut_help_messages = self._lut_help_messages
                    self.tcd._current_screen = self._current_instruction_set.screen_id
                    self.tcd._isVoiceMenu = False
                    # set is startup to False
                    self.tcd._isStartup = False
                else:
                    self.tcd._isVoiceMenu = True                
                self.launch(obj_factory.get(RLMenu, self.tcd, self.taskRunner), PROCESS_INSTRUCTIONS)
            elif self.tcd._tcode in self.tcd._voiceMenu.values():
                self.launch(obj_factory.get(self.tcd._tcode, self.tcd, self.taskRunner), PROCESS_INSTRUCTIONS)
            
        if self._instruction == None:
            ''' we've run out of instructions.  assume that the user wants to post'''
            self.next_state = POST_TO_HOST
            return
        else:
            if self._instruction.fieldid == 'ENDOFSESSION' or \
                    self.tcd._current_screen == 'ENDOFSESSION':
                ''' The operator said sign off.  Start over'''
                self._password_prefix_field_name  = None
                self._password_prefix_field_value = None
                self.tcd._current_screen = 'PT-INIT-Integrated'
                self.tcd._tcode = 'MENU'
                self.next_state = POST_INIT
                return     
            if self._instruction.command == 'Button' or self._instruction.command == 'Vocabulary' or \
                self._instruction.command == 'ScreenID' or self._instruction.command == 'Help':
                self.next_state = PROCESS_INSTRUCTIONS
                return
            ''' Get the additional vocabulary and confirmation prompts for this self._instruction group '''
            self._additional_vocabulary, self._confirmation_prompts = \
                self._current_instruction_set.get_additional_vocabulary_words(self._instruction.group)
            ''' Get the help_nessage for this self._instruction group '''
            self._help_message = self._lut_help_messages.get_message_by_group(self._instruction.group) 
            if self._instruction.command == 'SpeakPrompt':
                self.next_state = PROCESS_SPEAK_PROMPT
                return
            elif self._instruction.command == 'GetData': 
                ''' Note that the final part of the prompt could be contained in the getter '''
                self._what_to_speak = insert_space(self._what_to_speak,self._instruction.prompt) 
                self.next_state = GET_DATA_STATE
                return
            elif self._instruction.command == 'PassThrough':
                ''' PassThrough instructions allow us to send information to the host that may or 
                may not be in the html with out prompting the operator. '''  
                name, value = self._instruction.process(self._help_message, self._additional_vocabulary)
                ''' If fieldid is 'password-prefix', copy name/value returned from pass_through to 
                    self._password_prefix_field_name/self._password_prefix_field_value respectively.'''
                if self._instruction.fieldid == 'password-prefix':
                    self._password_prefix_field_name  = name
                    self._password_prefix_field_value = value
                else:
                    ''' Check if there is already an entry with the same 'name' in name/value pair dictionary.
                        If there is one, log a warning message.
                        (NOTE: name/value pairs will be updated with the latest entry)'''
                    if name in self._name_value_pairs:
                        log_message('Warning: Duplicate Name/Value entry in PT-INIT for fieldName "%s". Last entry (value = "%s") will be processed.' 
                                    % (name, value) )
                    self._name_value_pairs[name] = value
                self.next_state = PROCESS_INSTRUCTIONS
                return     
            elif self._instruction.command == 'SignOn': 
                ''' The SignOn instruction is "special". This command is used by the PT to determine
                when to get/send cookie information. ''' 
                # Jumex customization to handle use parsed operator ID for SAP password
                sapUserName = self.tcd.getCurrentSAPUser()
                if sapUserName == INVALID_OPERATOR_ID_FORMAT:
                    # this indicates that the operator ID does not conform to the proper format 
                    # of <resource>-<SAP user>
                    prompt_ready(itext(INVALID_OPERATOR_ID_FORMAT))
                    self.next_state = POST_INIT
                    return               
                self._name_value_pairs['sap-user']  = sapUserName
                self.next_state = POST_SIGNON
                return
            elif self._instruction.command == 'RePost': 
                ''' For the repost command the next state has to be adjusted based on 
                what is being reposted. '''
                if self._previous_command == 'SignOn':
                    self.next_state = POST_SIGNON
                elif self._previous_command == 'SignOff':
                    self.next_state = POST_SIGNOFF
                elif self._previous_command == 'Init':
                    self.next_state = POST_INIT
                else:
                    self.next_state = POST_TO_HOST
                ''' The previous name value pairs were saved in the post method above '''
                self._name_value_pairs = self._previous_name_value_pairs
                return

    #----------------------------------------------------------
    def post(self):
        ''' post the command to the PT.  NOTE: that ALL posts to the PT are handled by this method '''
        ''' Evaluate the operators response to the prompt.'''
        self._what_to_speak = ''
        try:
            self.current_operator = getenv('Operator.Name', '') 
                           
            self._lut.post(self._command, self._name_value_pairs,self.tcd.enableWorkerIDSuffix)
            
        except VoiceAttributeError as err:
            ''' We failed to build a valid instruction set.  This typically means that something went
            wrong in the build_instructions method of the VDERP Lut class.  Our only option is to 
            send the user back to the Welcome Prompt. This may result in orphaned  sessions on the 
            SAP side since we are not able to sign off first. Posting a sign off could be an option
            but it is not always in the available vocabulary '''
            self._report_voice_attribute_error(err.message)
            self.next_state = self.current_state
            return
        except Exception as err:
            ''' In all cases retry the post. 
                If we modify our application to send a transaction ID and we modify the service handler 
                on the SAP side to take advantage of this, we could potentially deal with this issue to avoid 
                duplicate posts.   ''' 
            ''' The previous name value pairs were saved in the post method above '''
            self._report_connection_error()
            
            if self._previous_command == 'SignOn':
                self.next_state = POST_TO_HOST
            elif self._previous_command == 'SignOff':
                self.next_state = POST_SIGNOFF
            elif self._previous_command == 'Init':
                self.next_state = POST_INIT
            else:
                self.next_state = POST_TO_HOST
            
            self._name_value_pairs['retry'] = "true"

          
                
            if 'sap-password' in self._name_value_pairs:
                self._name_value_pairs['sap-password'] = "XXX"
                if 'retry' in self._name_value_pairs:
                    del self._name_value_pairs['retry']
            if 'sap-Password' in self._name_value_pairs:
                self._name_value_pairs['sap-Password'] = "XXX"
                if 'retry' in self._name_value_pairs:
                    del self._name_value_pairs['retry']
            self._previous_name_value_pairs = self._name_value_pairs
            self._previous_command = self._command
            
            
            return
        ''' We got a valid response and instruction back from the host... process it 
        save the command and name/value pairs for processing below in the case of a 
        RePost command from an error screen. '''
        self._previous_command = self._command
        self._previous_name_value_pairs =self._name_value_pairs
        self._current_instruction_set = self._lut.get_instructions
        self._lut_help_messages = self._lut.get_help_messages
        self._name_value_pairs = {}
        self.next_state = PROCESS_INSTRUCTIONS
        ''' If this was a successful sign on the display a different page '''
        if (self._command == "SignOn"):
            ''' 
            Set the logged in  page that will be posted by the app when in this state. 
            This may not be accurate for the case where the operator has failed to give 
            the proper password. 
            '''
            set_display_page(self, LOGGED_IN)

#----------------------------------------------------------
# This line of code replaces the Processor class with the customization version
obj_factory.set_override(Processor, jumex_MLProcessor)
#----------------------------------------------------------
       
