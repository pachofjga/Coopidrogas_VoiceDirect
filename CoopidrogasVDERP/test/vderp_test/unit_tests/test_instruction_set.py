#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from vderp_test.unit_tests.BaseVDERPCommandTestCase import \
    BaseVDERPCommandTestCase
from commands.button import Button
from commands.get_data import GetData
from commands.speak_prompt import SpeakPrompt
from commands.vocabulary import Vocabulary
from instructions.instruction_set import InstructionSet
import unittest

''' This class tests the InstructionSet. '''

class TestInstructionSet(BaseVDERPCommandTestCase):
    '''
    The purpose of this test is to unit test all methods of the InstructionSet class
    
    We are not testing the "get_additional_vocabulary_words" method of the Instruction set
    class because it will be eaiser to test this method via functional tests.
    '''
 
    def setUp(self):
        self.clear()
        
                
    def test_instruction_set_init_method (self):
        ''' 
        Verify that the init method of the instruction set 
        creates a valid initial instruction set object
        '''        
        ''' Instantiate the instructinoSet object '''
        is_obj = InstructionSet()
        ''' verify that the instruction object has all of it's attributes '''
        self.assert_(hasattr(is_obj, '_list'), 'Instruction object does not have _list attribute')
        self.assert_(hasattr(is_obj, '_dict'), 'Instruction object does not have _dict attribute')
        self.assert_(hasattr(is_obj, '_dict_vcommand'), 'Instruction object does not have _dict_vcommand attribute')
        self.assert_(hasattr(is_obj, '_instruction_pointer'), 'Instruction object does not have _instruction_pointer attribute')
        self.assertEqual(is_obj.instruction_pointer, -1, 'Instruction pointer should be equal to -1')


    def test_instruction_pointer_setter(self):
        ''' 
        Verify that the setter for the instruction pointer never lets it's value
        become less than -1 or greater than the size of the instruction set.
        '''     
        ''' Instantiate the instructinoSet object '''
        instruction_set = InstructionSet()
        ''' try setting the pointer to a value that is out of range.'''
        ''' lowest allowable value is -1 '''
        instruction_set.instruction_pointer = -2
        ''' The setter should not allow the value of the instruction pointer to be < -1'''
        self.assertEqual(instruction_set._instruction_pointer, -1, 'Instruction pointer should be -1')
        ''' add two instructions to the instruction set '''
        instruction_set.add(self._create_get_numeric(1,1))
        instruction_set.add(self._create_get_numeric(1,2))
        ''' The instruction set now has a size of 2. 
        The setter should never allow the pointer value to become greater than the length of the ilst. 
        Try to set the pointer to 3. This should cause the pointer value to be set to the length of the list '''
        instruction_set.instruction_pointer = 3
        self.assertEqual(instruction_set._instruction_pointer, 2, 'Instruction Pointer should be two')
        ''' set instruction pointer to zero... this should work '''    
        instruction_set.instruction_pointer = 0
        self.assertEqual(instruction_set.instruction_pointer, 0, 'Could not set instruction pointer to zero')

    
    
    def test_reset_pointer_to_current_group(self):
        '''
        Verify that the instruction being pointed to is correct after doing an instruction_set reset.
        This is intended to confirm that we go to the first instruction in the group not first one 
        of the entire instruction set. ''' 
        
        ''' Put a couple of commands in the instruction set. Make at least one of them 
        in a different group than the rest
        '''
        ''' Instantiate the instructionSet object '''
        is_obj = InstructionSet()
        ''' Populate the instruction set with some commands in different groups '''
        sp = self._create_speak_prompt(1,1)
        is_obj.add(sp)
        sp = self._create_speak_prompt(1,2)
        is_obj.add(sp)
        ''' The next two are in group two '''
        sp = self._create_speak_prompt(2,1)
        is_obj.add(sp)
        sp = self._create_speak_prompt(2,2)
        is_obj.add(sp)
        v_obj = self._create_vocabulary('ready',1,3)
        is_obj.add(v_obj)
        v_obj = self._create_vocabulary('plant',1,4)
        is_obj.add(v_obj)
        ''' Iiterate through until pointing at 2nd speakprompt in group 2 '''
        is_obj.get_next_instruction() 
        is_obj.get_next_instruction() 
        is_obj.get_next_instruction() 
        is_obj.get_next_instruction() 
        ''' reset ''' 
        is_obj.reset_pointer_to_current_group()
        ''' this mimics the behavior in process_instructions '''
        ins = is_obj.get_next_instruction()
        ''' confirm that the current instruction is the first one in the group '''
        self.assertEqual(2, ins.group, "Group is not correct after reset. Expected: 2 Actual %d" % ins.group)
        self.assertEqual(1, ins.sequence, "Sequence is not correct after reset. Expected: 2 Actual %d" % ins.sequence)


    
    def test_add_method(self):
        ''' 
        Verify that we can successfully add instructions to the instruction set
        '''
        ''' Instantiate the instruction set object '''
        is_obj = InstructionSet()
        ''' Add a command to the instruction set that does not have a vocabword attribute.
            Nothing should be added to the vcommand dictionary for this instruction set. '''
        is_obj.add(self._create_get_numeric())
        ''' verify that the instruction got added to the list '''
        self.assertEqual(len(is_obj._list), 1, 'The list should only contain one instruction')
        ''' verify that the instruction got added to the dictionary '''
        self.assertEqual(len(is_obj._dict), 1, 'The dictionary should only contain one instruction')
        ''' verify that the vocabulary dictionary is empty. '''
        self.assertEqual(len(is_obj._dict_vcommand), 0, 'Vocabulary map should be empty')
        '''  Now add a valid Vocabulary command that the vocabword property is empty.
             Nothing should be added to the vcommand dictionary '''
        is_obj.add(self._create_vocabulary(''))
        ''' verify that the vocabulary dictionary is empty. '''
        self.assertEqual(len(is_obj._dict_vcommand), 0, 'Vocabulary map should be empty')
        '''  Now add a valid Vocabulary command '''
        is_obj.add(self._create_vocabulary('VCOMMAND001'))
        ''' verify that the vocabulary map contains the item. '''
        self.assertEqual(len(is_obj._dict_vcommand), 1, 'Vocabulary map should contain 1 entry')
        

    def test_get_instruction_by_fieldid(self):
        '''
        Verify that we can fetch an instruction by field id
        '''
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        ''' Add a command to the instruction set  '''
        instruction_set.add(self._create_get_numeric())
        ''' verify that we can fetch the instruction by field id. '''    
        self.assertIsNotNone(instruction_set.get_instruction_by_fieldid('field_id'), 'Did not find the requested instruction')
        try:
            instruction_set.get_instruction_by_fieldid('bogus_field_id')
            self.fail('Expected exception was not thrown')
        except ValueError as ve:
            self.assertEqual(str(ve), 'Instruction id bogus_field_id was not found', 'Incorrect error message')
        except:
            self.fail("The wrong exception was thrown")
      
        
    def test_get_previous_instruction(self):
        ''' 
        Verify that we always get the previous instruction or 'None' if we are out
        of range in the instruction set
        '''
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        self.assertIsNone(instruction_set.get_previous_instruction(),
                          "Instruction set is empty.  Should not have returned an instruction")        
        ''' Add some commands to the instruction set  '''
        instruction_set.add(self._create_speak_prompt(1, 1))
        instruction_set.add(self._create_speak_prompt(1, 2))
        instruction_set.add(self._create_get_numeric(1,3))
        '''  Try to get the previous instruction.  This should return 'None' because
        we haven't fetched the first instruction yet. ''' 
        self.assertIsNone(instruction_set.get_previous_instruction(), 'Should not have found an instruction.')
        ''' get the first instruction '''    
        first = instruction_set.get_next_instruction()
        ''' get the next instruction '''
        instruction_set.get_next_instruction()
        ''' get the previous instruction and verify that it is equal to the first instruction '''
        self.assertEqual(instruction_set.get_previous_instruction(), first, 'The incorrect instruction was recieved')
        ''' keep getting instructions until there are no more in the list.'''
        instruction_set.get_next_instruction()
        last_instruction = instruction_set.get_next_instruction()
        ''' the next call to get_next_instruction should return 'None'
            since we are at the end of the instruction set'''
        self.assertIsNone(instruction_set.get_next_instruction(),
                          "At end of instruction set, this call should have returned 'None'")
        ''' call get current instruction, should return 'None' '''
        self.assertEqual(instruction_set.get_previous_instruction(), last_instruction,
                         "Call to get previous instruction did not return the last instruction")

  
    def test_get_current_instruction(self):
        '''
        Verify that we always get the current instruction or we get 'None'
        if we are out of range in the instruction set.
        '''
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        ''' get_current_instruction should return 'None' since there are no instructions in the list. '''
        self.assertIsNone(instruction_set.get_current_instruction(),
                        "Instruction set is empty.  Should not have returned an instruction")        
        ''' Add some commands to the instruction set  '''
        instruction_set.add(self._create_speak_prompt(1, 1))
        instruction_set.add(self._create_speak_prompt(1, 2))
        instruction_set.add(self._create_get_numeric(1,3))
        '''  Try to get the current instruction.  This should return 'None' because
             we haven't fetched the first instruction yet. ''' 
        self.assertIsNone(instruction_set.get_current_instruction(), 'Should not have found an instruction.')
        ''' fetch the first instruction '''
        first = instruction_set.get_next_instruction()
        ''' verify that the current instruction is equal to the first instruction '''
        self.assertEqual(first, instruction_set.get_current_instruction(), 'Instructions were not equal')
        ''' keep getting instructions until there are no more in the list.'''
        instruction_set.get_next_instruction()
        instruction_set.get_next_instruction()
        ''' the next call to get_next_instruction should return 'None'
            since we are at the end of the instruction set'''
        self.assertIsNone(instruction_set.get_next_instruction(), "At end of instruction set, this call should have returned 'None'")
        ''' call get current instruction, should return 'None' '''
        self.assertIsNone(instruction_set.get_current_instruction(), "Call to get current instruction should did not return 'None'")


        
    def test_get_next_instruction(self):
        '''
        Verify that we always get the next instruction or we get 'None'
        if we are out of range in the instruction set.
        '''        
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        ''' get_next_instruction should return 'None' since there are no instructions in the list. '''
        self.assertIsNone(instruction_set.get_next_instruction(),
                        "Instruction set is empty.  Should not have returned an instruction")        
        ''' Add some commands to the instruction set  '''
        instruction_set.add(self._create_speak_prompt(1, 1))
        instruction_set.add(self._create_speak_prompt(1, 2))
        instruction_set.add(self._create_get_numeric(1,3))
        '''  Try to get the first instruction.  This should fetch the first instruction. ''' 
        first_instruction = instruction_set.get_next_instruction()
        ''' verify that we got the first instruciton in the list '''
        self.assertEqual(first_instruction, instruction_set._list[0], 'Did not get expected instruction.')
        ''' keep getting instructions until there are no more in the list.'''
        instruction_set.get_next_instruction()
        instruction_set.get_next_instruction()
        ''' the next call to get_next_instruction should return 'None'
            since we are at the end of the instruction set'''
        self.assertIsNone(instruction_set.get_next_instruction(), "At end of instruction set, this call should have returned 'None'")
    
    def test_get_action_by_vcommand(self):
        '''
        Verify that we can fetch an instruction by vcommand
        '''
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        ''' Add a vocabulary word to the instruction set  '''
        instruction_set.add(self._create_vocabulary("VRESERVE001", 1,1))
        ''' verify that we can fetch the instruction by "vcommandxxx" '''    
        self.assertIsNotNone(instruction_set.get_action_by_vcommand('VRESERVE001'), 'Did not find the requested instruction')
        ''' Try to fetch a command that is not in the the dictionary '''
        try:
            instruction_set.get_action_by_vcommand('VCOMMAND001')
            self.fail('Expected exception was not thrown')
        except ValueError as ve:
            self.assertEqual(str(ve), 'Command "VCOMMAND001" was not found', 'Incorrect error message')
        except:
            self.fail("The wrong exception was thrown")

 
    def test_get_description_list(self):
        '''
        Verify that we can get a list that contains the instructions used in by the 'description' command work
        '''
        ''' Instantiate the instruction set object '''
        instruction_set = InstructionSet()
        ''' verify that the description list is empty since the instruction set 
        does not contain any instructions '''    
        self.assertEqual(len(instruction_set.get_description_list()), 0, 'Description list is NOT empty')
        ''' Add a button to the instruction set that has the description attribute set to 1
        and has the fielddescription attribute set to "signoff button"  '''
        instruction_set.add(self._create_button("sign off", 1,1,1,'signoff button'))
        ''' add another instruction that does not have the description attribute '''
        instruction_set.add(self._create_get_numeric(1, 3))
        ''' verify that we get one instruction back in the list. '''    
        self.assertEqual(len(instruction_set.get_description_list()), 1, 'Should have one instruction in the list')
        ''' Add an instruction to the list that has the description attribute = 1 but the 
        fielddescription attribute is blank'''
        instruction_set.add(self._create_button("ready", 1,2,1,''))
        ''' get the description list.  this should fail because the fielddescription attribute is empty ''' 
        try:
            instruction_set.get_description_list()
            self.fail('Expected exception was not thrown')
        except ValueError as ve:
            self.assertEqual(str(ve),
                'Command "Button, button_field_id, button_field_name, button_field_value, 1, 2, ready, pre prompt, , , 0, , 1" description = 1 but field description was empty',
                'Incorrect error message')
        except:
            self.fail("The wrong exception was thrown")





    def _create_get_numeric(self, group=0, sequence=1):
        
        self.lut_data['command'] = 'GetNumeric'
        self.lut_data['fieldId'] = 'field_id'
        self.lut_data['fieldName'] = 'field_name'
        self.lut_data['fieldValue'] = 'field_value' 
        self.lut_data['group'] = group
        self.lut_data['sequence'] = sequence
        self.lut_data['prompt'] = 'This is a prompt'
        self.lut_data['validate'] = 0
        self.lut_data['validatePrePrompt'] = ''
        self.lut_data['validatePostPrompt'] = '' 
        self.lut_data['validatePriorityPrompt'] = 0 
        self.lut_data['confirmSpokenValue'] = 0
        self.lut_data['confirmSpokenValuePrePrompt'] = '' 
        self.lut_data['confirmSpokenValuePostPrompt'] = '' 
        self.lut_data['postButton'] = '' 
        self.lut_data['ready'] = 0 
        self.lut_data['minLength'] = 0
        self.lut_data['maxLength'] = 0
        self.lut_data['dataType'] = ''
        self.lut_data['fieldName2'] = ''
        self.lut_data['fieldId2'] = ''


       
        return  GetData(self.lut_data)

    def _create_vocabulary(self, vocab_word, group=0, sequence=1):
        
        self.lut_data['command']='Vocabulary'
        self.lut_data['fieldId'] = 'voc_field_id'
        self.lut_data['fieldName'] = 'voc_field_name'
        self.lut_data['fieldValue'] = 'voc_field_value' 
        self.lut_data['group'] = group
        self.lut_data['sequence'] = sequence
        self.lut_data['prePrompt']='prePrompt'
        self.lut_data['vocabWord']=vocab_word
                        
        return(Vocabulary(self.lut_data))
        
    def _create_speak_prompt(self, group=0, sequence=1):
        
        self.lut_data['command'] = 'SpeakPrompt'
        self.lut_data['prompt'] = 'This is a prompt'
        self.lut_data['prePrompt'] = 'pre prompt'
        self.lut_data['postPrompt'] = 'post prompt'
        self.lut_data['ready'] = 1
        self.lut_data['speakValue'] = 0
        self.lut_data['postButton'] = 'postButton'
        self.lut_data['group'] = group
        self.lut_data['sequence'] = sequence
         
        return(SpeakPrompt(self.lut_data))
    
    def _create_button(self, vocabword, group=0, sequence=1, description=0, field_description= ''):
        
        self.lut_data['command'] = 'Button'
        self.lut_data['fieldId'] = 'button_field_id'
        self.lut_data['fieldName'] = 'button_field_name'
        self.lut_data['fieldValue'] = 'button_field_value' 
        self.lut_data['group'] = group
        self.lut_data['sequence'] = sequence
        self.lut_data['vocabWord'] = vocabword        
        self.lut_data['description'] = description
        self.lut_data['fieldDescription'] = field_description
        self.lut_data['prePrompt'] = 'pre prompt'        
        self.lut_data['confirmSpokenValue'] = '0'
        self.lut_data['confirmSpokenValuePrePrompt'] = ''
        self.lut_data['confirmSpokenValuePostPrompt'] = ''                
         
        return(Button(self.lut_data))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
