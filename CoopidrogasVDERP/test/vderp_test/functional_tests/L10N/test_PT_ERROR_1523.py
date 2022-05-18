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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTExNTE2LjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTMxOTY0LjAwMy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","PT-ERROR-1523","","","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","PT-ERROR-1523","","","1","1","","","error.session.timed.out.message","","","","","","","","0","0","0","0","1","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","error.password.prompt","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',      # Password?
                                   '2!',           # Function?
                                   '1!',           # Work type?
                                   'VRESERVE001',  # Session timed out. Please sign on.  To continue say ready. 
                                   '-')            

    def test_en_US(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'en_US'
        #queue of LUT responses

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Work type?',
                              'Session timed out. Please sign on.  To continue say ready.',
                              'Password?')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTExNTE2LjAwMi4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTMxOTY0LjAwMy4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'])

        #validate log messages

    def test_de(self):
        mock_catalyst.environment_properties['SwVersion.Locale'] = 'de_DE'
        #queue of LUT responses


        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Willkommen beim Voice Direct ERP System. Aktueller Benutzer ist Operator.Name , Um fortzufahren, sagen Sie bereit.',
                              'Passwort?',
                              'Funktion?',
                              'taetigkeit wechseln?',
                              'Zeitüberschreitung. Bitte anmelden.',
                              'Passwort?')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"de_DE"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"DE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTExNTE2LjAwMi4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2bTFFVFpWZ0VNdTUxdDU5OGJaT3Bxa3pwTnZZZWZjWXdmLUFUVA==)/vowm_lm01/~flNUQVRFPTMxOTY0LjAwMy4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'])

        #validate log messages


if __name__ == '__main__':
    unittest.main()
