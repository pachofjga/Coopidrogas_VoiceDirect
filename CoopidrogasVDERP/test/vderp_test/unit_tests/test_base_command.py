#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.base_command import BaseCommand
import mock_catalyst
import unittest



class TestBaseCommand(BaseVDERPCommandTestCase):
    ''' 
    The the base_command constructor by:
    1. verifying the that the constructor initializes the base_command properties 
       to the values in the lut_data list.
    2. The type attribute is correct based on the command name
    3. Validate that the __str__ method constructs the expected string value
    '''
 
    def setUp(self):
        self.clear()
                        
    def testBaseCommand(self):
        
        '''
        Instantiate a BaseCommand object with the lut_data list. The lut_data list is 
        initialized to default values in the BaseVDERPCommandTestCase class.
        ''' 
        bcObj = BaseCommand(self.lut_data)
        
        '''
        Validate that the BaseCommand properties match the default lut_data values.
        '''
        self.assertEqual(bcObj.command,self.lut_data['command'])
        self.assertEqual(bcObj.fieldid,self.lut_data['fieldId'])
        self.assertEqual(bcObj.fieldname,self.lut_data['fieldName'])
        self.assertEqual(bcObj.group,self.lut_data['group'])
        self.assertEqual(bcObj.sequence,self.lut_data['sequence'])

        '''
        Verify that the BaseCommand.type attribute is set correctly based on the value of
        the lut_data['commmand'] field
        '''
        self.assertEqual(bcObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % bcObj.type)
        
        '''
        Construct the expected string that should be returned by the BaseCommand.__str__ method and
        and validate that it is the same as that returned by the call to BaseCommand.__str__()
        ''' 
        objString = '%s, %s, %s, %s, %d, %d' % \
            (self.command_name, self.field_id, self.field_name, self.field_value, self.group, self.sequence)     
        self.assertEqual(objString, bcObj.__str__())   
        
        ''' Verify that no log message was generated when this BaseCommand was created. '''
        if (len(mock_catalyst.log_messages) > 0):
            self.fail("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])
        
    def testInvalidBaseCommand(self):
        ''' 
        In this test verify that command type is 'None' when an unknown command is used to construct
        a BaseCommand object, and that the correct log message is generated.
        '''
        
        lut_data = self.lut_data
        
        ''' Initialize only command field of lut_data to an unknown command and use the 
        default values for the rest of the fields '''
        lut_data['command'] = 'invalid_command'
        
        ''' Instantiate the BaseCommand using the lut_data values '''  
        bcObj = BaseCommand(lut_data)
        
        ''' 
        Validate that the 'type' attribute is set to 'None' and that a log message has been generated
        indicating the problem.
        '''              
        self.assertTrue(bcObj.type == None, "Unexpected command type '%s'" % bcObj.type)
        
        self.assertTrue(len(mock_catalyst.log_messages) == 1,'Log message was not generated as expected')
        self.assertEqual('Unknown instruction type invalid_command', mock_catalyst.log_messages[0])
        

   
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
