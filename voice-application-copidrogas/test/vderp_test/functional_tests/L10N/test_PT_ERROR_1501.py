from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import
from main import main
import unittest
import mock_catalyst

class testSample(BaseVDERPTestCase):

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()

    def test_en_US(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'en_US'        
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-ERROR-1501","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","error.unexpected.message","","","","","correct.message","","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.please.sign.off.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","PT-ERROR-1501","","","1","1","","","","","","","","","","RLMOB-PMLGF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('-')  #  An unexpected error occurred.  See your system administrator.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('An unexpected error occurred.  See your system administrator.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])

        #validate log messages


    def test_de(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'de_DE'        
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-ERROR-1501","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","error.unexpected.message","","","","","correct.message","","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.please.sign.off.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","PT-ERROR-1501","","","1","1","","","","","","","","","","RLMOB-PMLGF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('-')  #  An unexpected error occurred.  See your system administrator.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Unerwarteter Fehler.  Wenden Sie sich an den Administrator.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'])

        #validate log messages

if __name__ == '__main__':
    unittest.main()
