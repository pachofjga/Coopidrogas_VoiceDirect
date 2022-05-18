'''
Created on Apr 21, 2016

@author: nconnors
'''
from voice import get_voice_application_property
from configparser import ConfigParser
import io
from voice import get_vad_path
from voice import log_message
from mlSharedConstants import AUTO_RUN_NOT_ACTIVE, AUTO_RUN_STATE,\
    AUTO_RUN_TCODE, RETURN_TCODE

#==============================================================================
class tcodeData(object):
    
    #--------------------------------------------------------------------------
    def __init__(self):
        ''' data common to all tcodes '''
        
        # initialize starting tcode task to MENU
        self._tcode = 'MENU' 
        
        self._current_instruction_set = None
        self._help_message = None
        self._what_to_speak = ''
        self._name_value_pairs = {}
        self._previous_name_value_pairs = {}
        self._lut = None
        self._command = None
        self._previous_command = None
        self._instruction = None
        self._additional_vocabulary = None
        self._confirmation_prompts = None
        self._word = None
        self._lut_help_messages = None
        self._current_screen = None
        self._previous_screen = None
        self._isStartup = True
        self._isVoiceMenu = False
        self._sapMenu = {}
        self._voiceMenu = {}
        
        # CR to be able to pick by eaches only
        self._pick_by_eaches_only = False

        self.initializeTaskPackageValues()

        self.loadIniConfig()
        
        # autoRun is a dictionary to be used when the current tcode
        # wishes to launch another tcode and then return to the current
        # tcode without the operator having to navigate the menu path.
        # The use case for implementing it is to add the ability for
        # an operator to print at the end of picking and then return to
        # the picking tcode after printing without having to navigate
        # the menu.
        self._autoRun = {AUTO_RUN_STATE:AUTO_RUN_NOT_ACTIVE, RETURN_TCODE:'', AUTO_RUN_TCODE:''}
                
        # dictionary containing screen names and button value to be posted to 
        # 'go back' / 'exit' the screen
        self.tcodeScreens = {}
        
        # if true indicates that a posting error was detected
        self._posting_error_detected = False

        self.v = {}

    #--------------------------------------------------------------------------
    def initializeTaskPackageValues(self):
        
        # initialize task package values
        # warehouse
        self._warehouse = get_voice_application_property('WarehouseID')
        # plant
        self._plant = get_voice_application_property('Plant')
                                        
        log_message('Task package values: warehouse = ' + self._warehouse + \
                    ', plant = ' + self._plant)

    #--------------------------------------------------------------------------
    def loadIniConfig(self):
        
        # Load the configuration file
        
        vad_path = get_vad_path()
        # remove 'task.vad' from the file pathname
        if 'task.vad' in vad_path:
            vad_path = vad_path.replace('task.vad','')
        # path sometimes has extra back slashes: 
        # \\Vocollect\\VocollectVoice\\Modules\\TaskRunner
        #    \\Data\\\\TaskPackages\\TaskDirectory\\task.vad\\resources
        # Get rid of the extra ones even though they don't seem to cause problems
        if '\\\\' in vad_path:
            vad_path = vad_path.replace('\\\\','\\')
        config_file = vad_path + "\\resources\\config.ini"
        with open(config_file) as f:
            ini_config = f.read()
        config = ConfigParser()
        config.readfp(io.StringIO(ini_config))

        self.getVoiceMenuData(config)
        
        self.getSAPMenuData(config)

    #--------------------------------------------------------------------------
    def getVoiceMenuData(self, config):
        
        # Retrieve voice menu for warehouse
        # limit data to current warehouse
        voice_menu_section = 'voice-menu-' + self._warehouse
        
        self._voiceMenu = {}
        
        # check to make sure that the section exists
        if config.has_section(voice_menu_section):
            for option,tcode in config.items(voice_menu_section):
                self._voiceMenu[int(option)] = tcode.upper()
            log_message('voiceMenu: ' + str(self._voiceMenu))
        else:
            # TODO: add error handler
            log_message('ERROR: config.ini missing voice menu section ' + voice_menu_section)
    
    #--------------------------------------------------------------------------
    def getSAPMenuData(self, config):
        
        # Retrieve SAP menu for warehouse
        # limit data to current warehouse
        sap_menu_section = 'SAP-menu-' + self._warehouse
        
        # check to make sure that the section exists
        if config.has_section(sap_menu_section):
        
            for tcode,val_1 in config.items(sap_menu_section):
                menuList = val_1.split(';')
                sequenceDict = {}
                for y in menuList:
                    seq, val_2 = y.split(':')
                    seqValuesDict = {}
                    for e in val_2.split(','):
                        name,value = e.split('=')
                        seqValuesDict[name] = value
                    sequenceDict[int(seq)] = seqValuesDict
                self._sapMenu[tcode.upper()] = sequenceDict
            log_message('sapMenu: ' + str(self._sapMenu))
        else:
            # TODO: add error handler
            log_message('ERROR: config.ini missing SAP menu section ' + sap_menu_section)
            
    #--------------------------------------------------------------------------
        
   
