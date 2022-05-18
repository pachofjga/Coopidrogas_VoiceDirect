from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import
from main import main
import unittest
import mock_catalyst

class testSample(BaseVDERPTestCase):

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()

        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","2","0","","say.password.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","password.prompt","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","PT-ERROR-1545","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","error.unexpected.message","","","","","correct.message","","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","PT-ERROR-1545","","","1","1","","","","","","","","","","RLMOB-PMLGF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
    def test_en_US(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'en_US'        
        #queue of LUT responses

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',      # Password?
                                   '-')            # Error in Voice Attributes file. Please see your device log, to continue, say ready

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'An unexpected error occurred.  See your system administrator.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'])

        #validate log messages

    def test_de(self):
        
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'de_DE'
        #queue of LUT responses

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',      # Password?
                                   '-')            # Error in Voice Attributes file. Please see your device log, to continue, say ready

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Willkommen beim Voice Direct ERP System. Aktueller Benutzer ist Operator.Name , Um fortzufahren, sagen Sie bereit.',
                              'Passwort?',
                              'Unerwarteter Fehler.  Wenden Sie sich an den Administrator.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"de_DE"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"DE"'])

        #validate log messages


if __name__ == '__main__':
    unittest.main()
