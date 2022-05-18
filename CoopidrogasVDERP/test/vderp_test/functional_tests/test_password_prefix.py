#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
# Verify that the password prefix functionality works as expected
from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, \
    BOTH_SERVERS #Needs to be first import
from main import main
import unittest

class testPasswordPrefix(BaseVDERPTestCase):
    '''
    Verify that the password prefix functionality works as expected
    '''

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()
        
    def testPasswordPrefix(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","",current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-Password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FSZndDWmRncE9tT282Y29VaHlQd3JKZVNBZmt3VmZWVi01ek1oNE1ELUFUVA==)/vowm_lm01/~flNUQVRFPTIzMjc5LjAwMi4wMS4wMQ====","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","Function?","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","ENDOFSESSION","","ENDOFSESSION","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","ENDOFSESSION","","ENDOFSESSION","1","1","","","Sign off successful","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","",current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-Password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '456!',          # Password?
                                   'VRESERVE002',   #'Function?'
                                   'VRESERVE003',   # VRESERVE002, correct?
                                   '-')             # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.   
        
        #run main application
        self.assertRaises(EndOfApplication, main)
        
        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'VRESERVE002, correct?',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.')
        
        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'],
                                      ['"SignOff"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FSZndDWmRncE9tT282Y29VaHlQd3JKZVNBZmt3VmZWVi01ek1oNE1ELUFUVA==)/vowm_lm01/~flNUQVRFPTIzMjc5LjAwMi4wMS4wMQ===="', '""', '"~OKCode"', '"/NEX"'],
                                      ['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])
        
    def testPasswordPrefixWrongFieldValue(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","",current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-Password","111","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","password.prompt","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","PT-ERROR-1521","","PT-ERROR-1521","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","error.say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","SpeakPrompt1","","","1","1","","","error.unable.login.message","error.try.again.message","","","","","","","0","0","0","0","1","0","0","0","","0"\r\n'
                                 '"Vocabulary","HELP","","","2","0","","say.password.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","password.prompt","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

 

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '456!',          # Password?
                                   'VRESERVE001',   # Unable to login. Please check your user name and password. , to try again, say ready.
                                   '-')             # Password? 
        
        #run main application
        self.assertRaises(EndOfApplication, main)
        
        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Unable to login. Please check your user name and password. , to try again, say ready.',
                              'Password?')
        
        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"111456"', '"sap-language"', '"EN"'])
        
    def testPasswordPrefixWrongFieldName(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","welcome.message","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","",current.operator.message","continue.say.ready3.message","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","password.prompt","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '456!',          # Password?
                                   '-')             #Error posting to host. See your system administrator. To try again, say ready.
                                   
        #run main application
        self.assertRaises(EndOfApplication, main)
        
        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Error posting to host. See your system administrator. To try again, say ready.')
        
        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])
                
    def testPasswordPrefix_fixWrongFieldName(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-Password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FSZndDWmRncE9tT282Y29VaHlQd3JKZVNBZmt3VmZWVi01ek1oNE1ELUFUVA==)/vowm_lm01/~flNUQVRFPTIzMjc5LjAwMi4wMS4wMQ====","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","Speak the function number,","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1, Put away","","0","0","0","0","0","1","0","0",""\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2, Picking","","0","0","0","0","0","1","0","0",""\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3, Inventory","","0","0","0","0","0","1","0","0",""\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","Function?","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","ENDOFSESSION","","ENDOFSESSION","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","ENDOFSESSION","","ENDOFSESSION","1","1","","","Sign off successful","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0",""\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"PassThrough","password-prefix","sap-Password","123","2","4","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0",""\r\n'
                                 '\n'
                                 '\n')
        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '456!',          # Password?
                                   'VRESERVE001',   # Error posting to host. See your system administrator. To try again, say ready.
                                   'VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '456!',          # Password?
                                   'VRESERVE002',   #'Function?'
                                   'VRESERVE003',   # VRESERVE002, correct?
                                   '-')             # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.   
        
        #run main application
        self.assertRaises(EndOfApplication, main)
        
        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Error posting to host. See your system administrator. To try again, say ready.',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'VRESERVE002, correct?',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.')
        
        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'],
                                      ['"SignOff"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FSZndDWmRncE9tT282Y29VaHlQd3JKZVNBZmt3VmZWVi01ek1oNE1ELUFUVA==)/vowm_lm01/~flNUQVRFPTIzMjc5LjAwMi4wMS4wMQ===="', '""', '"~OKCode"', '"/NEX"'],
                                      ['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])

if __name__ == '__main__':
    unittest.main()