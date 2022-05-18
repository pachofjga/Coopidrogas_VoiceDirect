#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.get_data import GetData
import mock_catalyst
import unittest


class TestGetData(BaseVDERPCommandTestCase):

    def setUp(self):
        print('running setup')
        self.clear()
                
        self.lut_data['command']='GetNumeric'
        self.lut_data['fieldValue']='2'

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
        self .lut_data['dataType'] = ''

    def testGetData(self):

        self.lut_data['validate']=1
        self.lut_data['validatePrePrompt']='validatePrePrompt'
        self.lut_data['validatePostPrompt']='validatePostPrompt' 
        self.lut_data['validatePriorityPrompt']=1 
        
        self.lut_data['confirmSpokenValue']=1
        self.lut_data['confirmSpokenValuePrePrompt']='confirmSpokenValuePrePrompt' 
        self.lut_data['confirmSpokenValuePostPrompt']='confirmSpokenValuePostPrompt' 
        
        self.lut_data['postButton']='postButton' 
        
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
        self.assertTrue(gdObj.priority_prompt, "Priority prompt should be false for GetData command")

        self.assertEqual(gdObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % gdObj.type)
        
        # validate str function
        objString = '%s, %s, %s, %s, %d, %d, %s, %s, %s' % \
            ('GetData', self.field_id, self.field_name, self.lut_data['fieldValue'], self.group, self.sequence, \
             self.lut_data['prompt'], self.lut_data['ready'], self.lut_data['postButton'])     
        self.assertEqual(objString, gdObj.__str__())  
        
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'"  % mock_catalyst.log_messages[0])


    def testGetDataNumericBasicDialog(self):
        # queue up some responses to your prompts 
        self.post_dialog_responses('2!')
        
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


    def testGetDataNumericReadyDialog(self):
        # queue up some responses to your prompts 
        self.post_dialog_responses('2VRESERVE001')
        
        self.lut_data['ready']=1 

        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        #check that the prompt was spoken correctly
        self.validate_prompts('This is a prompt')

    def testGetDataNumericValidateDialog(self):
        # queue up some responses to your prompts 
        self.post_dialog_responses('2VRESERVE001','5VRESERVE001')
        
        # configure lut data for to do validation prompts
        self.lut_data['validatePrePrompt']='Validate pre prompt'
        self.lut_data['validatePostPrompt']='validate post prompt' 
        self.lut_data['validate']=1
        self.lut_data['fieldValue'] = '5'
        
        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        

    def testGetDataNumericMinGreaterMaxDialog(self):
        # queue up some responses to your prompts 
        ''' the purpose of this test is to check if Value Error exception is thrown '''
        ''' if a Value Error exception is thrown when min > max ''' 
        self.post_dialog_responses('123VRESERVE001')
        
        self.lut_data['ready']=1 
        self.lut_data['fieldValue'] = '123'
        self.lut_data['minLength'] = 3
        self.lut_data['maxLength'] = 1

        try:
            GetData(self.lut_data)
        except ValueError:
            if(len(mock_catalyst.log_messages) == 0):        
                print("Expected log message not generated")
            else:
                objString = 'Min Length greater than max length for command GetNumeric'
                self.assertEqual(objString, mock_catalyst.log_messages[0])
            

    def testGetDataNumericNoReadyDialog(self):
        # queue up some responses to your prompts 
        ''' the purpose of this test is to Check the if ready is not set dialog'''
        ''' the operator has to speak the min length to move on''' 
        self.post_dialog_responses('123!')
        
        self.lut_data['ready']=0
        self.lut_data['minLength'] = 3
        self.lut_data['maxLength'] = 10
        self.lut_data['fieldValue']='123'

        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        #check that the prompt was spoken correctly
        self.validate_prompts('This is a prompt')

    def testGetDataNumericGreaterThanMaxDialog(self):
        # queue up some responses to your prompts 
        ''' the purpose of this test is to Check the if max is set then words spoken'''
        ''' greater than the max length are ignored''' 
        self.post_dialog_responses('1234567!')
        
        self.lut_data['ready']=0
        self.lut_data['fieldValue'] = '123456'
        self.lut_data['minLength'] = 3
        self.lut_data['maxLength'] = 6

        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        #check that the prompt was spoken correctly
        self.validate_prompts('This is a prompt')

    def testGetDataNumericConfirmDialog(self):
        # queue up some responses to your prompts 
        self.post_dialog_responses('5VRESERVE001','VRESERVE003')
        
        # configure lut data for to do confirmation prompts
        self.lut_data['confirmSpokenValue']=1
        self.lut_data['confirmSpokenValuePrePrompt']='Confirm spoken value pre prompt' 
        self.lut_data['confirmSpokenValuePostPrompt']='Confirm spoken value post prompt' 
        self.lut_data['fieldValue'] = '5'
        
        gnObj = GetData(self.lut_data)

        response = self.runCommand(gnObj)   

        # test the the returned values. 
        self.assertTrue(self.field_name==response[0], \
                        "Wrong field name. Actual: %s Expected: %s" % (self.field_name,response[0]))
        self.assertTrue(self.lut_data['fieldValue'] == response[1][0], \
                        "Wrong field value. Actual: '%s' Expected: '%s'" % (self.field_value,response[1][0]))
        
        #check that the prompts were spoken correctly
        self.validate_prompts('This is a prompt', 'Confirm spoken value pre prompt <Spell>5</Spell>, Confirm spoken value post prompt')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
