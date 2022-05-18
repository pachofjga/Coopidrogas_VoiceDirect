#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import
from main import main
import unittest
import mock_catalyst

class testSample(BaseVDERPTestCase):

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()

    def test_en_US(self):

        mock_catalyst.environment_properties['SwVersion.Locale'] = 'Aen_US'
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-ERROR-1525","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","error.try.again.say.ready2.message","","","","","correct.message","","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.please.say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","SpeakPrompt1","","","1","1","","","error.invalid.language.code.message","","","","","","","RLMOB-PMLGF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","3","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        
        #queue of Dialog Responses
        self.post_dialog_responses('-')           

       
        
        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
#       self.validate_prompts('Task contains invalid language code. See your system administrator. , to try again, say ready.')
                             

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"Aen_US"', '""', '""', '""', '""', '""', '""'])

        #validate log messages



    def test_de(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'de_A'
                #queue of LUT responses
        self.set_server_response('"ScreenID","PT-ERROR-1525","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","error.try.again.say.ready2.message","","","","","correct.message","","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","SpeakPrompt1","","","1","1","","","error.invalid.language.code.message","","","","","","","RLMOB-PMLGF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","3","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        
        #queue of Dialog Responses
        self.post_dialog_responses('-')           

        self.assertRaises(EndOfApplication, main)

        #validate prompts
#       self.validate_prompts('Task enthält ungültige Sprachbausteine. Wenden Sie sich an den Administrator. , Zum wiederholen sagen Sie Bereit.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_A"', '""', '""', '""', '""', '""', '""'])

        #validate log messages




if __name__ == '__main__':
    unittest.main()
