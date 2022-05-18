#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
'''
Created on Jan 31, 2013

@author: amukherjee
'''
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.get_data import GetData
import mock_catalyst
import unittest


class TestGetDataAlphaNumeric(BaseVDERPCommandTestCase):

    def setUp(self):
        print('running setup')
        self.clear()
                
        self.lut_data['command']='GetBarCode'
        self.lut_data['fieldValue']='123ABC'

        self.lut_data['prompt']='This is a prompt'
        
        self.lut_data['validate']=0
        self.lut_data['validatePrePrompt']=''
        self.lut_data['validatePostPrompt']='' 
        self.lut_data['validatePriorityPrompt']=0 
        
        self.lut_data['confirmSpokenValue']=0
        self.lut_data['confirmSpokenValuePrePrompt']='' 
        self.lut_data['confirmSpokenValuePostPrompt']='' 
        
        self.lut_data['postButton']='' 
        self.lut_data['ready']=0 
        self.lut_data['minLength']=0
        self.lut_data['maxLength']=0        



    def testGetData(self):
        
        ''' the purpose of this test is to ensure that all the fields in the LUT data is set correctly and also the string object
            has the right elements '''

        self.lut_data['validate']=1
        self.lut_data['validatePrePrompt']='validatePrePrompt'
        self.lut_data['validatePostPrompt']='validatePostPrompt' 
        self.lut_data['validatePriorityPrompt']=1 
        
        self.lut_data['confirmSpokenValue']=1
        self.lut_data['confirmSpokenValuePrePrompt']='confirmSpokenValuePrePrompt' 
        self.lut_data['confirmSpokenValuePostPrompt']='confirmSpokenValuePostPrompt' 
        
        self.lut_data['postButton']='postButton' 
        '''Ensuring that the legacy data types pass the unit test 
           The test case for the legacy data type and Get Data only differs in the command and the dataType field being populated 
        '''
        self.lut_data['command'] = 'GetBarCode'
        
        gdObj = GetData(self.lut_data)
        
        self.assertEqual(gdObj.prompt, self.lut_data['prompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.prompt, self.lut_data['prompt']))
        self.assertEqual(gdObj.ready, self.lut_data['ready'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.ready, self.lut_data['ready']))
        self.assertEqual(gdObj.minlength, 0, \
                         "Actual: '%d' Expected: '%d" % (gdObj.minlength, 0))
        self.assertEqual(gdObj.maxlength, 0, \
                         "Actual: '%d' Expected: '%d'" % (gdObj.maxlength, 0))
        self.assertEqual(gdObj.validatepriorityprompt, self.lut_data['validatePriorityPrompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.validatepriorityprompt, self.lut_data['validatePriorityPrompt']))
        self.assertEqual(gdObj.validatepostprompt, self.lut_data['validatePostPrompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.validatepostprompt, self.lut_data['validatePostPrompt']))
        self.assertEqual(gdObj.validatepreprompt, self.lut_data['validatePrePrompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.validatepreprompt, self.lut_data['validatePrePrompt']))
        self.assertEqual(gdObj.validate, self.lut_data['validate'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.validate, self.lut_data['validate']))
        self.assertEqual(gdObj.confirmspokenvaluepostprompt, self.lut_data['confirmSpokenValuePostPrompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.confirmspokenvaluepostprompt, self.lut_data['confirmSpokenValuePostPrompt']))
        self.assertEqual(gdObj.confirmspokenvaluepreprompt, self.lut_data['confirmSpokenValuePrePrompt'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.confirmspokenvaluepreprompt, self.lut_data['confirmSpokenValuePrePrompt']))
        self.assertEqual(gdObj.confirmspokenvalue, self.lut_data['confirmSpokenValue'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.confirmspokenvalue, self.lut_data['confirmSpokenValue']))
        self.assertEqual(gdObj.postbutton, self.lut_data['postButton'], \
                         "Actual: '%s' Expected: '%s" % (gdObj.postbutton, self.lut_data['postButton']))
        self.assertTrue(gdObj.barcode, "Bar code should be true for GetbarCode command")
        self.assertFalse(gdObj.priority_prompt, "Priority prompt should be false for GetbarCode command")
        
        ''' Verify that the constructor updated the legacy command to a GetData with correct dataType setting '''
        self.assertEqual(gdObj.datatype, 'AlphaNumeric', \
                         "Actual: '%s' Expected: '%s" % (gdObj.datatype, 'AlphaNumeric'))
        self.assertEqual(gdObj.command, 'GetData', \
                         "Actual: '%s' Expected: '%s" % (gdObj.command, 'GetData'))

        self.assertEqual(gdObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % gdObj.type)
         
        # validate str function
        objString = '%s, %s, %s, %s, %d, %d, %s, %s, %s' % \
            ('GetData', self.field_id, self.field_name, self.lut_data['fieldValue'], self.group, self.sequence, \
             self.lut_data['prompt'], self.lut_data['ready'], self.lut_data['postButton'])     
        self.assertEqual(objString, gdObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])


    def testGetDataAlphaBasicDialog(self):
        # queue up some responses to your prompts 
        ''' this function tests the basic functionality to ensure that the spoken field 
        value equals the expected field value'''
        self.post_dialog_responses('123ABC!')
        
        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        
        #check that the prompt was spoken correctly
        # the prompts list contains two elements for each prompt.
        # one is the actual prompt spoken and one is whether the
        # prompt was a priority prompt.
        self.validate_prompts('This is a prompt')


    def testGetDataAlphaReadyDialog(self):
        # queue up some responses to your prompts 
        ''' the purpose of this test is to Check the ready dialog'''
        ''' the ready bit is set to 1 and then after speaking the field value the operator
        needs to speak ready to move on''' 
        self.post_dialog_responses('123ABCVRESERVE001')
        
        self.lut_data['ready']=1 
        self.lut_data['fieldValue'] = '123ABC'

        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        
        #check that the prompt was spoken correctly
        self.validate_prompts('This is a prompt')


    def testGetDataAlphaValidateDialog(self):
        # queue up some responses to your prompts 
        ''' the purpose of this test is to verify that the validate dialog works as expected
        The test is made by speaking the wrong field value and checking that the response builds correctly
        The validatePrePrompt has values that are spoken before the field value
        The validatePostPrompt has values that are spoken after the field value
        One needs to speak ready to move to after speaking the field value'''
        
        self.post_dialog_responses('123PQR','123ABC')
        
        # configure lut data for to do validation prompts
        self.lut_data['validatePrePrompt']='Validate pre prompt'
        self.lut_data['validatePostPrompt']='validate post prompt' 
        self.lut_data['validate']=1
        self.lut_data['fieldValue'] = '123ABC'
        
        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        
        #check that the prompts were spoken correctly
        self.validate_prompts('This is a prompt', 'Validate pre prompt <Spell>123PQR</Spell>, validate post prompt')
        
    def testGetDataAlphaConfirmDialog(self):
        # queue up some responses to your prompts 
        '''Tests to verify if the confirm dialog behaves correctly if the confirm bit is set.
        confirmSpokenValuePrePrompt has values that are spoken before the field value is spoken
        confirmSpoekenValuePostPrompt has values that are spoken after the field value
        Expected response after the field value is YES '''
        self.post_dialog_responses('123ABCVRESERVE001','VRESERVE003')
        
        # configure lut data for to do confirmation prompts
        self.lut_data['confirmSpokenValue']=1
        self.lut_data['confirmSpokenValuePrePrompt']='Confirm spoken value pre prompt' 
        self.lut_data['confirmSpokenValuePostPrompt']='Confirm spoken value post prompt' 
        self.lut_data['fieldValue'] = '123ABC'
        
        gnObj = GetData(self.lut_data)
        
        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        
        #check that the prompts were spoken correctly
        self.validate_prompts('This is a prompt', 'Confirm spoken value pre prompt <Spell>123ABC</Spell>, Confirm spoken value post prompt')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
