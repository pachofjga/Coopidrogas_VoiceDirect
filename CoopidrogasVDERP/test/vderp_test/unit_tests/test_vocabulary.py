#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import \
    BaseVDERPCommandTestCase
from commands.vocabulary import Vocabulary
import mock_catalyst
import unittest


class TestVocabulary(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        
        self.lut_data['command']='Vocabulary'
        self.lut_data['prePrompt']='prePrompt'
        self.lut_data['vocabWord']='vocabWord'
         
                        
    def testVocabulary(self):

        vObj = Vocabulary(self.lut_data)
    
        self.assertEqual(vObj.type, 'Action', "Invalid command type. Actual: '%s' Expected: 'Action'" % vObj.type)
        
        # validate str function
        objString = "%s, %s, %s, %s, %d, %d, %s, %s" % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence, \
             self.lut_data['vocabWord'], self.lut_data['prePrompt'])     
        self.assertEqual(objString, vObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

        # verify properties
        self.assertEqual(self.lut_data['vocabWord'], vObj.vocabword)
        self.assertEqual(self.lut_data['prePrompt'], vObj.preprompt)
        
            
   
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
