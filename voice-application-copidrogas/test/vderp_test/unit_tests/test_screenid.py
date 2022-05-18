#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.screen_id import ScreenId
import mock_catalyst
import unittest



class TestScreenId(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        
        self.lut_data['command']='ScreenID'
        self.lut_data['prePrompt']='url'
        self.lut_data['prompt']='cookie' 
         
                        
    def testScreenId(self):

        sidObj = ScreenId(self.lut_data)
    
        ''' Check properties '''
        self.assertEqual(self.lut_data['prePrompt'], sidObj.url)
        self.assertEqual(self.lut_data['prompt'], sidObj.cookie)
        
        ''' verify command type '''
        self.assertEqual(sidObj.type, 'ScreenId', "Invalid command type. Actual: '%s' Expected: 'ScreenId'" % sidObj.type)
        
        # validate str function
        objString = '%s, %s, %s, %s, %d, %d, %s, %s' % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence, \
             self.lut_data['prePrompt'], self.lut_data['prompt'])     
        self.assertEqual(objString, sidObj.__str__())  
        
        ''' no log messages expected here '''
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])

        a_url = 'aUrl'
        a_cookie = 'aCookie'
    
        sidObj.url = a_url
        sidObj.cookie = a_cookie

        ''' Check property setters '''
        self.assertEqual(a_url, sidObj.url)
        self.assertEqual(a_cookie, sidObj.cookie)
            
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
