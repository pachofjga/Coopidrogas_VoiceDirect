from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import
from main import main
import unittest

class testSerial(BaseVDERPTestCase):

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()

    def testSerial(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","2","0","","say.password.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-user","sap-user",".serial","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","password.prompt","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc2N2pTZzh3QjBLcWFhN0VYcjJ","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '654321!',      # Password?
                                   '-')            # Function?

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Device.Id"', '"sap-Password"', '"654321"', '"sap-language"', '"EN"'])

        #validate log messages

if __name__ == '__main__':
    unittest.main()
