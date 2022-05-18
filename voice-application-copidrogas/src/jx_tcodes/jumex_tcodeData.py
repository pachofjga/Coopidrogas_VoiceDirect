'''
Created on Aug 1, 2017

@author: nconnors
'''

from voice import get_voice_application_property
from configparser import ConfigParser
import io
from voice import get_vad_path, getenv
from voice import log_message
from vocollect_core.utilities.localization import itext
from vocollect_core.dialog.functions import prompt_ready
from tcodes.tcodeData import tcodeData
from vocollect_core.utilities import obj_factory
from mlSharedConstants import INVALID_OPERATOR_ID_FORMAT

#==============================================================================
class jumex_tcodeData(tcodeData):
    
    #--------------------------------------------------------------------------
    def __init__(self):
        ''' data common to all tcodes '''
        
        # get TTS language code
        self.language = getenv('SwVersion.Locale', 'en_US')
        
        super(jumex_tcodeData, self).__init__()
        
    #--------------------------------------------------------------------------
    def initializeTaskPackageValues(self):
        
        # initialize task package values
        # warehouse
        self._warehouse = get_voice_application_property('WarehouseID')
        # plant
        self._plant = get_voice_application_property('Plant')
        # password confirmation required?
        self.confirmPassword = get_voice_application_property('ConfirmPasswordInput') == 'true'
        # require HU confirmation?
        self.confirmHU = get_voice_application_property('ConfirmHURequired') == 'true'
        # require batch confirmation?
        self.confirmBatch = get_voice_application_property('ConfirmBatchRequired') == 'true'
        # auto select 1st menu entry if only one entry exists
        self.autoSelectMenuIfOneEntry = get_voice_application_property('AutoSelectMenuIfOneEntry') == 'true'
        # variable used in conjunction with autoSelectMenuIfOneEntry.  If autoSelectMenuIfOneEntry is True and
        # signOffRequest is also True then sign off is automatically executed.  Otherwise, only existing menu
        # entry is executed
        self.signOffRequest = False
        # enable use of SAP user by multiple voice users.  This works for multiple users as long as only one
        # voice user is logged on at a time.  The VoiceConsole operator ID is parsed at the first hyphen
        # into 2 strings.  The first string is the SAP user ID that is posted to SAP at sign on.
        self.enableWorkerIDSuffix = get_voice_application_property('EnableWorkerIDSuffix') == 'true'
        
        # location parse key
        # at Jumex the location components are referred to as:
        #    A = aisle
        #    S = stack
        #    L = level
        # the key specifies how the location prompt will be spoken.
        # A hyphen between components indicates that they will be spoken using
        # separate voice prompts.  Components without a hyphen will be spoken
        # at the same voice prompt.
        self.locationParsingkey = get_voice_application_property('LocationParsingKey')
        # There are only 4 valid location parse key values: 'A-S-L', 'AS-L', 'A-SL' and 'ASL'
        # Verify that parameter has been defined correctly:
        if self.locationParsingkey not in ['A-S-L', 'AS-L', 'A-SL','ASL']:
            # invalid location parse key - cannot continue - this is a fatal error
            #  do not let the task flow continue - operator must load new task package
            while True:
                prompt_ready(itext('error.fatal.load.new.task'))
                prompt_ready(itext('error.invalid.location.parse.key', self.locationParsingkey)) 
        else:
            # initialize speak aisle/stack prompt values
            # speak aisle
            self.speakAislePrompt = False
            if self.locationParsingkey == 'A-S-L' or self.locationParsingkey == 'A-SL':
                self.speakAislePrompt = True
            # speak stack
            self.speakStackPrompt = False
            if self.locationParsingkey == 'A-S-L' or self.locationParsingkey == 'AS-L':
                self.speakStackPrompt = True
            # level prompt is always spoken if it is different from the last pick
            
        log_message('Task package values: warehouse = ' + self._warehouse + \
                    ', plant = ' + self._plant + ', Confirm password input = ' + str(self.confirmPassword) + \
                    ', confirm HU required = ' + str(self.confirmHU) + ', confirm batch required = ' + \
                    str(self.confirmBatch) + ', Location parse key = ' + self.locationParsingkey)

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
        config_file = vad_path + "/resources/config.ini"
        with open(config_file) as f:
            ini_config = f.read()
        config = ConfigParser()
        config.readfp(io.StringIO(ini_config))

        self.getVoiceMenuData(config)
        
        self.getSAPMenuData(config)

    #--------------------------------------------------------------------------
    def getSAPMenuData(self, config):
        
        # Retrieve SAP menu for warehouse
        # limit data to current warehouse
        sap_menu_section = 'SAP-menu-' + self._warehouse
        
        # retrieve language specific menu data
        if self.language != 'en_US':
            sap_menu_section += '-' + self.language

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
                        seqValuesDict[name] = value.upper()
                    sequenceDict[int(seq)] = seqValuesDict
                self._sapMenu[tcode.upper()] = sequenceDict
            log_message('sapMenu: ' + str(self._sapMenu))
        else:
            # TODO: add error handler
            log_message('ERROR: config.ini missing SAP menu section ' + sap_menu_section)
            
    #--------------------------------------------------------------------------
    def getCurrentSAPUser(self):
        ''' method is used to always retrieve current operator ID from environment variable
             to avoid problems with old data if buttons are used to load a new user '''
        
        # to minimize issues with invalid operator ID format do some simple checks
        splitOperatorId = getenv('Operator.Id').split('-')
        # abarradas operatorId might come without resource
        #if len(splitOperatorId) != 2:
            # indicates invalid operator ID format
            # return error
            #return INVALID_OPERATOR_ID_FORMAT
        return splitOperatorId[0]
    
    #--------------------------------------------------------------------------
    def getCurrentSAPResource(self):
        ''' method is used to always retrieve current operator ID from environment variable
             to avoid problems with old data if buttons are used to load a new user '''
        
        # to minimize issues with invalid operator ID format do some simple checks
        splitOperatorId = getenv('Operator.Id').split('-')
        if len(splitOperatorId) != 2:
            # indicates invalid operator ID format
            # return error
            return INVALID_OPERATOR_ID_FORMAT
        return splitOperatorId[1]
    
    #--------------------------------------------------------------------------



        
#This line of code replaces the tcodeData class with the customization version
obj_factory.set_override(tcodeData, jumex_tcodeData)
   
