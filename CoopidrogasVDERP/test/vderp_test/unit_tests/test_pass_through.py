#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
import mock_catalyst
from commands.pass_through import PassThrough
from vderp_test.unit_tests.BaseVDERPCommandTestCase import \
    BaseVDERPCommandTestCase
import unittest



class TestHelp(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        

        self.lut_data['command']='PassThrough'
                        
    def testPassThrough(self):
        ''' 
        This test case verifies that the PassThrough command is created correctly
        using default lut_data that is initialized in the BaseVDERPCommandTestCase
        class. The standard __str__ command is validated.
        '''   

        passThroughObj = PassThrough(self.lut_data)
    
        self.assertEqual(passThroughObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % passThroughObj.type)
        
        # validate str function
        objString = "%s, %s, %s, %s, %d, %d" % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence)     
        self.assertEqual(objString, passThroughObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

        # this is limited because getEnv is not implemented in mock_catalyst
        passThroughObj.fieldvalue = 'dummy'
        response = self.runCommand(passThroughObj)
        
        self.assertEqual('dummy', response[1])
        
    def testPassThroughLanguageCodeNotDefined(self):
        ''' 
        This test case verifies that the PassThrough command works correctly 
        with respect to the .languageCode field value. 
        In this test case verify that if the LanguageMap is not set correctly
        the default language code is returned and appropriate log messages 
        are generated
        '''   

        ''' Set the fieldValue to allow testing of the .languageCode functionality '''
        self.lut_data['fieldValue'] = '.languageCode'
        self.lut_data['fieldName'] = 'sap-language'
        
        ''' Set the device locale '''
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'en_US'
        ''' Clear the LanguageMap to cause the languageCode not found condition '''
        mock_catalyst.application_properties['LanguageMap'] = None

        ''' Instantiate the pass-through command '''
        passThroughObj = PassThrough(self.lut_data)
            
        ''' RUn the command with the lut data specified '''
        response = self.runCommand(passThroughObj)
        
        ''' Verify that the default language code was returned since the correct 
            one was not found in the LanguageMap. '''
        self.assertEqual('en_US', response[1], 
                         "Default language code does not match. Expected 'EN' Actual: '%s'" % response[1])
        
        ''' Make sure the log messages were generated '''
        self.assertTrue(len(mock_catalyst.log_messages) != 0,"Expected log messages were not generated.")
        ''' And that they contain the correct text '''
        self.assertEqual('Error in LanguageMap Project Property; please check your Voice Configuration file.', 
                             mock_catalyst.log_messages[0], 'Incorrect log message generated')
            
    def testPassThroughLanguageCode(self):
        ''' 
        This test case verifies that the PassThrough command works correctly with
        respect to the .languageCode fieldValue. This test case verifies correct 
        behavior for the case when the LanguageMap is configured. 
        '''   

        ''' Set locale to something different than the default '''
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'es_MX'
        ''' Populate the LanguageMap Project Property '''
        mock_catalyst.application_properties['LanguageMap'] = "[('en_US','EN'),('de','DE'),('fr','FR'),('es_MX','1X'),('it','IT'),('pt_BR','PT'),('es','ES')]"
        
        ''' Set fieldValue and fieldName for .languageCode case ''' 
        self.lut_data['fieldValue'] = '.languageCode'
        self.lut_data['fieldName'] = 'sap-language'
        
        ''' Instantiate pass-thgough command '''
        passThroughObj = PassThrough(self.lut_data)
    
        ''' Run the pass through command using the lut date provided '''
        response = self.runCommand(passThroughObj)
        
        ''' Verify that the correct language code was returned '''
        self.assertEqual('1X', response[1], "LanguageCode does not match. Expected: '1X' Actual: '%s'" % response[1])
        
        ''' Should not be any log messages generated '''
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

    def testDeviceId(self):
        ''' 
        This test case verifies that the PassThrough command works correctly with
        respect to passing device id instead of operator id.  
        '''   

        ''' Set Device.Id in environment_properties'''
        mock_catalyst.environment_properties['Device.Id'] = '123456'
        
        ''' Set fieldValue and fieldName for .serial ''' 
        self.lut_data['fieldValue'] = '.serial'
        self.lut_data['fieldName'] = 'sap-user'
        
        ''' Instantiate pass-through command '''
        passThroughObj = PassThrough(self.lut_data)
    
        ''' Run the pass through command using the lUT date provided '''
        response = self.runCommand(passThroughObj)
        
        ''' Verify that 'Device Id' was returned '''
        self.assertEqual('123456', response[1], "Device ID not passed. Expected: '123456' Actual: '%s'" % response[1])
                         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
