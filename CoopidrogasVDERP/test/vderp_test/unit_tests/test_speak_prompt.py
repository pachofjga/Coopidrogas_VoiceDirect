#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import BaseVDERPCommandTestCase
from commands.speak_prompt import SpeakPrompt
import mock_catalyst
import unittest


'''
Test the SpeakPrompt command by:
1. Validate the constructor, properties and __str__.
2. Run the SpeakPrompt.process method and validate the returned values.
'''
class TestSpeakPrompt(BaseVDERPCommandTestCase):

 
    def setUp(self):
        self.clear()
        
        ''' Set default values for the lut_data '''
        self.lut_data['command'] = 'SpeakPrompt'
        self.lut_data['prompt'] = 'This is a prompt'
        self.lut_data['prePrompt'] = 'pre prompt'
        self.lut_data['postPrompt'] = 'post prompt'
        self.lut_data['ready'] = 1
        self.lut_data['speakValue'] = 0
        self.lut_data['postButton'] = 'postButton'
         
                        
    def testSpeakPrompt(self):
        ''' Test that the command attributes and __str__ method return the correct values based on the lut_data '''
        
        ''' Create a SpeakPrompt command object using the already initialized lut_data '''
        spObj = SpeakPrompt(self.lut_data)
    
        ''' Verify that the SpeakPrompt properties are initialized correctly by the constructor 
            by comparing them with the lut_data.'''
        self.assertEqual(spObj.preprompt, self.lut_data['prePrompt'], \
                         "Actual: '%s' Expected: '%s" % (spObj.preprompt, self.lut_data['prePrompt']))
        self.assertEqual(spObj.prompt, self.lut_data['prompt'], \
                         "Actual: '%s' Expected: '%s" % (spObj.prompt, self.lut_data['prompt']))
        self.assertEqual(spObj.postprompt, self.lut_data['postPrompt'], \
                         "Actual: '%s' Expected: '%s" % (spObj.postprompt, self.lut_data['postPrompt']))
        self.assertEqual(spObj.speakvalue, self.lut_data['speakValue'], \
                         "Actual: '%s' Expected: '%s" % (spObj.speakvalue, self.lut_data['speakValue']))
        self.assertEqual(spObj.ready, self.lut_data['ready'], \
                         "Actual: '%s' Expected: '%s" % (spObj.ready, self.lut_data['ready']))
        self.assertEqual(spObj.postbutton, self.lut_data['postButton'], \
                         "Actual: '%s' Expected: '%s" % (spObj.postbutton, self.lut_data['postButton']))

        ''' Verify that the 'type' attribute is set correctly. It should be 'Command' for a SpeakPrompt '''
        self.assertEqual(spObj.type, 'Command', "Invalid command type. Actual: '%s' Expected: 'Command'" % spObj.type)
        
        ''' Validate the __str__ function '''
        objString = '%s, %s, %s, %s, %d, %d, %s, %s, %s, %d, %d, %s' % \
            (self.lut_data['command'], self.field_id, self.field_name, self.field_value, self.group, self.sequence, \
             self.lut_data['prePrompt'], self.lut_data['prompt'], self.lut_data['postPrompt'], \
             self.lut_data['ready'], self.lut_data['speakValue'], self.lut_data['postButton'])     
        self.assertEqual(objString, spObj.__str__())  
        
        ''' Confirm that no unexpected log messages are generated '''
        if(len(mock_catalyst.log_messages) != 0):        
            print("Unexpected log message generated: '%s'" % mock_catalyst.log_messages[0])


    def testSpeakPromptComplete(self):
        ''' Test that when the 'ready' attribute is set the prompt_is_complete indicator is set to True.'''

        ''' 
        Instantiate a SpeakPomrpt command object using the lut_data set in the set_up method.
        This lut_data has the 'ready' field set to 1.
        '''
        spObj = SpeakPrompt(self.lut_data)
        
        '''
        Call the process method of the SpeakPrompt command and get the returned values. The
        process method is called from the BaseVDERPCommandTestCase.runCommand method.
        '''
        (what_to_speak, prompt_is_complete) = self.runCommand(spObj)
        
        '''
        Confirm that the 'prompt_is_complete' flag is set to true and that the 'what_to_speak'
        variable is set to the values from the prompt and post-prompt field of the lut_data.
        '''
        self.assertTrue(prompt_is_complete, "'prompt_is_complete' is NOT set to True")
        self.assertEqual(self.lut_data['prompt']+' '+self.lut_data['postPrompt'], what_to_speak)
        
        
    def testSpeakPromptSpeakValueOperator(self):
        ''' Verify correct behavior for .operator in fieldvalue and ready set to 0'''       

        ''' Set lut_data for this case. '''
        self.lut_data['fieldValue'] = '.operator'  
        self.lut_data['ready'] = 0   
        self.lut_data['speakValue'] = 1 
        
        ''' Instantiate SpeakPrompt command using the lut_data'''
        spObj = SpeakPrompt(self.lut_data)
        
        '''Invoke the process method of the SpeakPrompt command'''
        (what_to_speak, prompt_is_complete) = self.runCommand(spObj)
        
        ''' 
        Verify that prompt_is_complete is set to False since ready is set to 1.
        Confirm that the prompt is correct with the fieldValue inserted between the 
        prompt and post-prompt.
        '''
        self.assertFalse(prompt_is_complete, "'prompt_is_complete' IS set")
        self.assertEqual('This is a prompt Operator.Name post prompt', what_to_speak)
        
        
    def testSpeakPromptSpeakValue(self):
        ''' Verify correct behavior for fieldValue populated with something besides .operator.'''       

        ''' Initialize the lut_data setting the fielValue to a number and speakValue to 1'''
        self.lut_data['fieldValue'] = '25'  
        self.lut_data['ready'] = 0   
        self.lut_data['speakValue'] = 1 
        
        ''' Instantiate the SpeakPomrpt command object using the lut_data'''
        spObj = SpeakPrompt(self.lut_data)
        
        ''' Call SpeakPrompt.process with the instantiated object '''
        (what_to_speak, prompt_is_complete) = self.runCommand(spObj)
        
        ''' Validate the prompt is prompt+fieldValue+post-prompt'''
        self.assertEqual('This is a prompt '+self.lut_data['fieldValue']+' post prompt', what_to_speak)
        

    def testSpeakPromptEmptyPrompt(self):
        ''' Verify correct behavior for no prompt value set'''       

        ''' Clear the prompt field in the lut_data'''
        self.lut_data['prompt'] = ''
        self.lut_data['ready'] = 0  
        
        ''' Instantiate the SpeakPrompt command''' 
        spObj = SpeakPrompt(self.lut_data)
        
        ''' Run the SpeakPrompt process method'''
        (what_to_speak, prompt_is_complete) = self.runCommand(spObj)
        
        ''' Confirm that what_to_say is set to just the post prompt '''
        self.assertEqual('post prompt', what_to_speak)
        
        
    def testSpeakPromptEmptyPostPrompt(self):
        ''' Verify correct behavior for post prompt filed being empty'''       

        ''' Clear the prompt field in the lut_data'''
        self.lut_data['postPrompt'] = ''
        self.lut_data['ready'] = 0   
        
        ''' Instantiate the SpeakPrompt command''' 
        spObj = SpeakPrompt(self.lut_data)
        
        ''' Run the SpeakPrompt process method'''
        (what_to_speak, prompt_is_complete) = self.runCommand(spObj)
        
        ''' Confirm that what_to_say is set to just the prompt '''
        self.assertEqual('This is a prompt', what_to_speak)
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
