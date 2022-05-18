#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.help import Help
import mock_catalyst
import unittest



class TestHelp(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        
        self.lut_data['command']='Help'
        self.lut_data['prePrompt']='prePrompt'
         
                        
    def testButton(self):

        helpObj = Help(self.lut_data)
    
        self.assertEqual(helpObj.type, 'Help', "Invalid command type. Actual: '%s' Expected: 'Help'" % helpObj.type)
        
        # validate str function
        objString = "%s, %s, %s, %s, %d, %d, '%s'" % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence, \
             self.lut_data['prePrompt'])     
        self.assertEqual(objString, helpObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

        # verify properties
        self.assertEqual(self.lut_data['prePrompt'], helpObj.message)
        
        a_help_message = 'Help me!'
        helpObj.message = a_help_message
        self.assertEqual(a_help_message, helpObj.message)
        
            
   
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
