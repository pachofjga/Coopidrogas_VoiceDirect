#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
from mock_catalyst import get_vad_path 
import glob
import re
import unittest


class TestPropertyKeys(unittest.TestCase):
    
    

    def test_for_duplicate_keys_in_PromptMapping_files(self):
        '''
        Test that there are no duplicate keys in a given PromptMapping file
        '''
        path = get_vad_path()

        prompt_mapping_file_path = path +  'resources\\translations\\'
        language_codes = {}
        
        ''' Get all the properties files '''
        files = glob.glob(prompt_mapping_file_path+'*.properties')
        
        for file in files:
            '''
            Find PrompMapping files for each language code and save them.
            ''' 
            m = re.match(r'^.*?PromptMapping(?P<lang_code>_\w{2}(_\w{2})?)\.properties',file)
            if (m):
                language_codes[m.group('lang_code')] = file
                 
        ''' Add the default property file '''
        language_codes['default'] = prompt_mapping_file_path+'PromptMapping.properties'
        

        for code in language_codes:
            ''' Now check each PromptMapping file ''' 
            prop_file = open(language_codes[code])
            print('Checking file: %s' % (prop_file.name))
            
            lines = prop_file.readlines();
            duplicate_keys = self.check_for_duplicate_key(lines)
                        
            prop_file.close()
            if len(duplicate_keys) > 0:
                self.fail('Duplicate key(s): %s found in file: %s\n' % (duplicate_keys,prop_file.name))
            
            
    def check_for_duplicate_key(self, lines):
        '''
        list(str) -> list(str)
        Loop through each line and save the property key. If
        any key is encountered twice then save in a duplicate_keys
        list. Return the duplicate_keys list.
        '''
        properties = {}
        duplicate_keys = []
        for line in lines:
            if line.find('=') > 0:
                key, value = line.split('=')
                if len(properties) > 0 and key in properties:
                    if len(duplicate_keys) > 0:
                        duplicate_keys.append(key)
                    else:
                        duplicate_keys = [key]
                else:
                    properties[key] = value
        
        return duplicate_keys


if __name__ == "__main__":
    unittest.main()
