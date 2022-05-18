#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from BaseVDERPTestCase import BaseVDERPTestCase
from instructions.help_messages import HelpMessages
from mock_catalyst import EndOfApplication
import sys
import traceback

#expected values


class BaseVDERPCommandTestCase(BaseVDERPTestCase):
    '''
    Base class for VDERP command unit test cases
    '''

    def __init__(self, methodName):
        super(BaseVDERPCommandTestCase, self).__init__(methodName)
        '''
        Constructor
        '''
        self._command_name='GetData'
        self._field_id='field_id'
        self._field_name='field_name'
        self._field_value='field_value'
        self._group=1
        self._sequence=2

        self._lut_data = {}
        self._lut_data['command']=self._command_name
        self._lut_data['fieldId']=self._field_id
        self._lut_data['fieldName']=self._field_name
        self._lut_data['fieldValue']=self._field_value 
        self._lut_data['group']=self._group
        self._lut_data['sequence']=self._sequence
        self._lut_data['hint']=''
        self._lut_data['isUom']=0
        
    @property    
    def command_name(self):
        return self._command_name

    @property    
    def field_id(self):
        return self._field_id


    @property    
    def field_name(self):
        return self._field_name


    @property    
    def field_value(self):
        return self._field_value


    @property    
    def group(self):
        return self._group


    @property    
    def sequence(self):
        return self._sequence

    @property    
    def lut_data(self):
        return self._lut_data

    def runCommand(self, obj, additional_vocabulary = {}, confirmation_prompts = {} ):
        ''' obj - the command object
            confirmation_prompts - any additional confirmation prompts need by get_data
        '''
        response = ()
            
        # GetNumeric.process needs a helpmessage object
        hmsgs = HelpMessages()
        helpmessage = hmsgs.get_message_by_group(0)
        
        try:
            if(obj.command == 'GetData'):
                response = obj.process(obj.prompt,helpmessage, additional_vocabulary, confirmation_prompts)
            else:
                response = obj.process(helpmessage, None)
        except:
            print("Exception in user code:")
            print('-' * 60)
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            print('-' * 60)
            assert sys.exc_info()[0] == EndOfApplication

         
        return response

