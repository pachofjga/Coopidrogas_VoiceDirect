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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc0UHBtVWdhRHFSdEtEWGkteEtIdlZxa3pxMXVZZHFBS2xsLUFUVA==)/vowm_lm01/~flNUQVRFPTE0NDY5LjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumericA","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',       # Password?
                                   'talkman help',  # Error in Voice Attributes file. Please see your device log, to continue, say ready.
                                   '-')             # Error in Voice Attributes file. Please see your device log, to continue, say ready.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Error in Voice Attributes file. Please see your device log, to continue, say ready.',
                              'say ready.',
                              'Error in Voice Attributes file. Please see your device log, to continue, say ready.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'])

        #validate log messages


    def test_de(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'de_DE'
        #queue of LUT responses
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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc0UHBtVWdhRHFSdEtEWGkteEtIdlZxa3pxMXVZZHFBS2xsLUFUVA==)/vowm_lm01/~flNUQVRFPTE0NDY5LjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumericA","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',       # Password?
                                   'talkman help',  # Error in Voice Attributes file. Please see your device log, to continue, say ready.
                                   '-')             # Error in Voice Attributes file. Please see your device log, to continue, say ready.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Willkommen beim Voice Direct ERP System. Aktueller Benutzer ist Operator.Name , Um fortzufahren, sagen Sie bereit.',
                              'Passwort?',
                              'Fehler in den Sprachattributen. Bitte überprüfe das Gerätelogfile, um fortzufahren, sag fertig.',
                              'Sagen Sie Bereit.',
                              'Fehler in den Sprachattributen. Bitte überprüfe das Gerätelogfile, um fortzufahren, sag fertig.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"de_DE"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"DE"'])

        #validate log messages



if __name__ == '__main__':
    unittest.main()
