#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.button import Button
import mock_catalyst
import unittest



class TestButton(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        
        self.lut_data['command']='Button'
        self.lut_data['vocabWord']='vocabWord' 
        self.lut_data['prePrompt']='prePrompt'
        self.lut_data['confirmSpokenValuePrePrompt']='confirmSpokenValuePrePrompt' 
        self.lut_data['confirmSpokenValuePostPrompt']='confirmSpokenValuePostPrompt' 
        self.lut_data['fieldDescription']='fieldDescription'
        self.lut_data['confirmSpokenValue']=1
        self.lut_data['description']='description'
         
                        
    def testButton(self):

        buttonObj = Button(self.lut_data)
    
        self.assertEqual(buttonObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % buttonObj.type)
        
        # validate str function
        objString = '%s, %s, %s, %s, %d, %d, %s, %s, %s, %s, %s, %s, %s' % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence, \
             self.lut_data['vocabWord'], self.lut_data['prePrompt'], self.lut_data['confirmSpokenValuePrePrompt'],\
             self.lut_data['confirmSpokenValuePostPrompt'], self.lut_data['confirmSpokenValue'], \
             self.lut_data['fieldDescription'], self.lut_data['description'])     
        self.assertEqual(objString, buttonObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

            
        response = self.runCommand(buttonObj)
        self.assertEquals(self.lut_data['prePrompt'],response[0])
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
