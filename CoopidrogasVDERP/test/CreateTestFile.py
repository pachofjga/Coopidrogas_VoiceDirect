#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
import mock_catalyst

class CreateTestFile():
    
    def __init__(self, test_name='Sample', mock_server = None):
        self.test_name = test_name
        self.mock_server = mock_server
        
    
    def create_test_case(self):

        result = []
                    
        result.append('from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import')
        result.append('from main import main')
        result.append('import unittest')
        result.append('')
        result.append('class test'+self.test_name+'(BaseVDERPTestCase):')
        result.append('')    
        result.append('    def setUp(self):')
        result.append('        self.start_server(BOTH_SERVERS)')
        result.append('        self.clear()')
        result.append('')    
        result.append('    def test%s(self):' % self.test_name)
        
        #----------------------------------------------------------------------
        if self.mock_server is not None:
            result.append('        #queue of LUT responses')
            for response in self.mock_server._server_responses_sent:
                response = response.replace('\r\n', '\\r\\n')
                response = response.replace('\r', '\\r')
                response = response.replace('\n', '\\n')
                response = response.replace("\\n", "\\n'\n                                 '")
                response = "        self.set_server_response('%s')" % response
                response = response.replace("\n                                 '')", ')')
                result.append(response)
            result.append('')
        
        #----------------------------------------------------------------------
        result.append('        #queue of Dialog Responses')
        count = 0
        eol = ','
        max = 0
        for response_pair in mock_catalyst.responses_to_prompts:
            if len(response_pair[0]) > max:
                max = len(response_pair[0])

        for response_pair in mock_catalyst.responses_to_prompts:
            response = response_pair[0]
            if count == len(mock_catalyst.responses_to_prompts) - 1:
                eol = ')'
            if count == 0:
                output = "        self.post_dialog_responses('" + response + "'" + eol
            else:
                output = "                                   '" + response + "'" + eol
            result.append(output.ljust(40 + max)  + "# " + response_pair[1])
            count += 1
        result.append('')
        
        result.append('        #run main application')
        result.append("        self.assertRaises(EndOfApplication, main)")
        result.append("")
        
        #----------------------------------------------------------------------
        result.append('        #validate prompts')
        count = 0
        eol = ','
        for prompt in mock_catalyst.prompts:
            if count == len(mock_catalyst.prompts) - 1:
                eol = ')'
            if count == 0:
                result.append("        self.validate_prompts('" + prompt[0] + "'" + eol)
            else:
                result.append("                              '" + prompt[0] + "'" + eol)
            count += 1
        result.append('')
        
        #----------------------------------------------------------------------
        if self.mock_server is not None:
            result.append('        #validate LUT Requests')
            count = 0
            for request in self.mock_server._server_requests:
                request = request.replace('\n', '')
                request = request.replace('\r', '')
                
                #break up lut
                
                parts = request.split(",")
                commandName = parts.pop(0)
                
    
                #remove unwanted params
                date = parts.pop(0) #@UnusedVariable
                date = parts.pop(0) #@UnusedVariable
                date = parts.pop(0) #@UnusedVariable
                                
                if count == 0:
                    command = "        self.validate_server_requests(['%s'" % commandName
                else:
                    command = "                                      ['%s'" % commandName
                
                ''' 
                Since the real operatorid was in the SignOn request when the test case was initially created 
                the field value must be replaced with Operator.Id to be used for in the generated case. 
                Handle both Integrated and Standalone ITS parameter names.
                '''
                if (commandName=='"SignOn"'):
                    if('"sap-user"' in parts):
                        parts[parts.index('"sap-user"')+1]='"Operator.Id"'
                    elif('"~login"' in parts):
                        parts[parts.index('"~login"')+1]='"Operator.Id"'
                    
                    
                for param in parts:
                    command = command + ", '" + param  + "'"
    
                if count == len(self.mock_server._server_requests) - 1:
                    command = command + "])"
                else:
                    command = command + "],"
                result.append(command)
                count += 1
            result.append('')

        #----------------------------------------------------------------------
        result.append('        #validate log messages')
        result.append('')    
        result.append("if __name__ == '__main__':")
        result.append('    unittest.main()')
        
        return result

    def write_test_to_file(self, file_path = ''):
        f = open(file_path + 'test' + self.test_name + '.py', 'w', encoding='utf-8')
        output = self.create_test_case()
        for line in output:
            f.write(line + '\n')
        f.close()
        
