#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from BaseVDERPTestCase import BaseVDERPTestCase
from LUT.VDERPLut import VDERPLut
from LUT.voice_attribute_error import VoiceAttributeError
from vocollect_lut_odr_test.mock_server import BOTH_SERVERS
import unittest


class testVDERPLut(BaseVDERPTestCase):

 
    def setUp(self):
        self.clear()
        self.start_server(BOTH_SERVERS)
        self.clear()
 
                        
    def test_VDERPLut_init(self):
        ''' this test verifies that the all the attributes have been created correctly'''
        self._lutObj = VDERPLut()
    
        ''' verify that the instruction object has all of it's attributes '''
        
        self.assert_(hasattr(self._lutObj, 'object_types'), 'Instruction object does not have object types')
        self.assert_(hasattr(self._lutObj, '_instruction_set'), 'Instruction object does not have _instruction_set')
        self.assert_(hasattr(self._lutObj, '_help_messages'), 'Instruction object does not have _help_messages')
        self.assert_(hasattr(self._lutObj, '_screenId'), 'Instruction object does not have _screenId')
        self.assert_(hasattr(self._lutObj, '_lut_transport'), 'Instruction object does not have _lut_transport attribute')
        self.assert_(hasattr(self._lutObj, '_lut_formatter'), 'Instruction object does not have _lut_formatter attribute')
        self.assert_(hasattr(self._lutObj, '_lut_data'), 'Instruction object does not have _lut_data attribute')
        self.assert_(hasattr(self._lutObj, '_lut_connection'), 'Instruction object does not have _lut_conection attribute')
        
    def test_VDERPLut_objectType(self): 
        
        ''' the purpose of the test case is to verify that the object type is created correctly'''
        
        ''' Check for the length to ensure that no object types can be randomly added or removed'''    
        lutObj = VDERPLut()
        num_objects = 11
        self.assert_((lutObj.object_types.__len__(),num_objects),"Incorrect number of object types")
        
        ''' verifies that all the object types have been defined '''
        self.assertIn("ScreenID", lutObj.object_types, "ScreenId not defined in object types") 
        self.assertIn("Help", lutObj.object_types, "Help not defined in object types")
        self.assertIn("SpeakPrompt", lutObj.object_types, "Speak Prompt not defined in object types") 
        self.assertIn("GetData", lutObj.object_types, "Get Data not defined in object types")
        self.assertIn("GetNumeric", lutObj.object_types, "GetNumeric not defined in object types")
        self.assertIn("GetAlpha", lutObj.object_types, "GetAlpha not defined in object types")       
        self.assertIn("GetAlphaNumeric", lutObj.object_types, "GetAlphaNumeric not defined in object types")
        self.assertIn("GetBarCode", lutObj.object_types, "GetBarCode not defined in object types")
        self.assertIn("Button", lutObj.object_types, "Button not defined in object types")
        self.assertIn("Vocabulary", lutObj.object_types, "Vocabulary not defined in object types")
        self.assertIn("PassThrough", lutObj.object_types, "PassThrough not defined in object types")
        self.assertIn("SignOn", lutObj.object_types, "SignOn not defined in object types")  
           
    #   add check for the size
    
    
    
    
    
    def test_VDERPLut_post(self):
        
        ''' This test ensures that the exceptions that coreect exception is thrown when someting
            goes wrong when converting a lut response into python opbjects.  If the objects are 
            not built correctly the post method will throw an exception depending on the error.'''
        
        lutObj = VDERPLut()
        ''' Test that we can successfully build response without throwing an exception'''
        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        ''' Verify the the call to "post" does NOT throw an exception 
            If we catch an exception here, fail the test because an exception
            should not have been thrown.''' 
        try:
            lutObj.post('Init',[])
        except Exception as e:
            self.fail('An unexpected exception ' + str(e) + ' was thrown')
        except VoiceAttributeError as e:
            self.fail('An unexpected VoiceAttributeError ' + str(e.message) + ' was thrown')
            
        
        ''' Verify that an incorrect command name causes the post method to throw a VoiceAttribute 
            exception.  Create an invalid command by mis-spelling SpeakPrompt as SpeaksPrompt.
            The post method should throw a VoiceAttributeException'''
        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeaksPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        ''' Verify the the call DOES throw an exception '''
        try:
            lutObj.post('Init',[])
            self.fail('An expected VoiceAttributeError was not thrown')
        except Exception as e:
            self.fail('An unexpected exception was thrown.')
        except VoiceAttributeError as err:
            ''' Verify that the error message is correct '''
            self.assertEqual('Error: Unknown command name "SpeaksPrompt" for screen "PT-INIT-Integrated"', \
                              err.message, 'Incorrect error message was found')
                                    
            
        
        ''' Verify that setting minlength greater that maxlength on a GetNumeric command causes an exception
            to be thrown. '''
        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","6","3","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        ''' Verify the the call DOES throw an exception '''
        try:
            lutObj.post('Init',[])
            self.fail('An expected VoiceAttributeError was not thrown')
        except Exception as e:
            self.fail('An unexpected exception was thrown.')
        except VoiceAttributeError as err:
            ''' Verify that the error message is correct '''
            self.assertEqual('Error: minlength cannot be greater than maxlength in command "GetNumeric" for screen "PT-INIT-Integrated"', \
                              err.message, 'Incorrect error message was found')
                                    


        ''' Return an empty server response to the post command to simulate a "time out"
            We should catch an Exception here.'''
        
        self.set_server_response("")
        
        ''' Verify the the call DOES throw an exception '''
        try:
            lutObj.post('Init',[])
            self.fail('An expected Exception was not thrown')
        except Exception as e:
            self.assertEqual('timed out',  str(e), 'Incorrect error message was found')
        except VoiceAttributeError as err:
            self.fail('An unexpected VoiceAttributeError was thrown.')

        

        
        
    def test_VDERPLut_lut_data(self):
        
        ''' the purpose of the test case is to check that the lut data is created correctly
        Check for the length to ensure that the lut data has all the right attributes
        Check for the index of the fields added to ensure that the attributes have been added in the right location'''
        
        lutObj = VDERPLut()
        num_of_elements = 26
        # add the size check
        lut_data = lutObj._lut_data.fields
        self.assertEqual(lut_data.__len__(),num_of_elements,"Inconsistent number of elements in Lut Data")
        ''' for each value of the lut check to see if the field name and the index of the Lut value is consistent'''
        self.assertEqual("command", lut_data['command'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['command'].name, "command"))
        self.assertEqual(0, lut_data['command'].index)
        
        self.assertEqual("fieldId", lut_data['fieldId'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['fieldId'].name, "fieldId"))
        self.assertEqual(1, lut_data['fieldId'].index)
        
        self.assertEqual("fieldName", lut_data['fieldName'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['fieldName'].name, "fieldName"))
        self.assertEqual(2, lut_data['fieldName'].index)
        
        self.assertEqual("fieldValue", lut_data['fieldValue'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['fieldValue'].name, "fieldValue"))
        self.assertEqual(3, lut_data['fieldValue'].index)
        
        self.assertEqual("group", lut_data['group'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['group'].name, "group"))
        self.assertEqual(4, lut_data['group'].index)
        
        self.assertEqual("sequence", lut_data['sequence'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['sequence'].name, "sequence"))
        self.assertEqual(5, lut_data['sequence'].index)
        
        self.assertEqual("vocabWord", lut_data['vocabWord'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['vocabWord'].name, "vocabWord"))
        self.assertEqual(6, lut_data['vocabWord'].index)
        
        self.assertEqual("prePrompt", lut_data['prePrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['prePrompt'].name, "prePrompt"))
        self.assertEqual(7, lut_data['prePrompt'].index)
        
        self.assertEqual("prompt", lut_data['prompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['prompt'].name, "prompt"))
        self.assertEqual(8, lut_data['prompt'].index)
        
        self.assertEqual("postPrompt", lut_data['postPrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['postPrompt'].name, "postPrompt"))
        self.assertEqual(9, lut_data['postPrompt'].index)
        
        self.assertEqual("validatePrePrompt", lut_data['validatePrePrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['validatePrePrompt'].name, "validatePrePrompt"))
        self.assertEqual(10, lut_data['validatePrePrompt'].index)
        
        self.assertEqual("validatePostPrompt", lut_data['validatePostPrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['validatePostPrompt'].name, "validatePostPrompt"))
        self.assertEqual(11, lut_data['validatePostPrompt'].index)
        
        self.assertEqual("confirmSpokenValuePrePrompt", lut_data['confirmSpokenValuePrePrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['confirmSpokenValuePrePrompt'].name, "confirmSpokenValuePrePrompt"))
        self.assertEqual(12, lut_data['confirmSpokenValuePrePrompt'].index)
        
        self.assertEqual("confirmSpokenValuePostPrompt", lut_data['confirmSpokenValuePostPrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['confirmSpokenValuePostPrompt'].name, "confirmSpokenValuePostPrompt"))
        self.assertEqual(13, lut_data['confirmSpokenValuePostPrompt'].index)
        
        self.assertEqual("fieldDescription", lut_data['fieldDescription'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['fieldDescription'].name, "fieldDescription"))
        self.assertEqual(14, lut_data['fieldDescription'].index)
        
        self.assertEqual("postButton", lut_data['postButton'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['postButton'].name, "postButton"))
        self.assertEqual(15, lut_data['postButton'].index)
        
        self.assertEqual("validate", lut_data['validate'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['validate'].name, "validate"))
        self.assertEqual(16, lut_data['validate'].index)
        
        self.assertEqual("validatePriorityPrompt", lut_data['validatePriorityPrompt'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['validatePriorityPrompt'].name, "validatePriorityPrompt"))
        self.assertEqual(17, lut_data['validatePriorityPrompt'].index)
        
        self.assertEqual("confirmSpokenValue", lut_data['confirmSpokenValue'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['confirmSpokenValue'].name, "confirmSpokenValue"))
        self.assertEqual(18, lut_data['confirmSpokenValue'].index)
        
        self.assertEqual("speakValue", lut_data['speakValue'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['speakValue'].name, "speakValue"))
        self.assertEqual(19, lut_data['speakValue'].index)
        
        self.assertEqual("ready", lut_data['ready'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['ready'].name, "ready"))
        self.assertEqual(20, lut_data['ready'].index)
        
        self.assertEqual("description", lut_data['description'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['description'].name, "description"))
        self.assertEqual(21, lut_data['description'].index)
        
        self.assertEqual("minLength", lut_data['minLength'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['minLength'].name, "minLength"))
        self.assertEqual(22, lut_data['minLength'].index)
        
        self.assertEqual("maxLength", lut_data['maxLength'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['maxLength'].name, "maxLength"))
        self.assertEqual(23, lut_data['maxLength'].index)
        
        self.assertEqual("hint", lut_data['hint'].name, \
                         "Actual: '%s' Expected: '%s" % (lut_data['hint'].name, "hint"))
        self.assertEqual(24, lut_data['hint'].index)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
