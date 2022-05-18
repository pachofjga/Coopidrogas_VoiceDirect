#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------

''' Needs to be first import '''
from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication,  BOTH_SERVERS 
from main import main
import mock_catalyst
import unittest

class test_Processor(BaseVDERPTestCase):


    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()


    def test_button_error_getters(self):
        
        ''' The purpose of this test is to verify that we throw a "Error in voice attributes" message back to the user
            if they mis-spell the button ID in the post butto property of a "Getter".  '''
        
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        ''' Set the postButton property of the GetNumeric command to "BUTTON-DOES-NOT-EXIST."
            The value should really be "RLMOB-PNEXT".
            The VAD will fail to find the button in the response and should throw an error message back to the user  '''
        
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc0WFFRdGxwMXpnbEgzdjY4Mm5","SX3hxa3pwZXVvY0t5djA4LUFUVA==)/vowm_lm01/~flNUQVRFPTU5MTIuMDAyLjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","BUTTON-DOES-NOT-EXIST","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc0WFFRdGxwMXpnbEgzdjY4Mm5","SX3hxa3pwZXVvY0t5djA4LUFUVA==)/vowm_lm01/~flNUQVRFPTU5MTIuMDAyLjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","BUTTON-DOES-NOT-EXIST","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')


        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',       # Password?
                                   '2!',            # Function
                                   'VRESERVE001',   # Error
                                   '-')             # Function 

        ''' run main application '''
        self.assertRaises(EndOfApplication, main)
        
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Error in Voice Attributes file. Please see your device log, to continue, say ready.',
                              'Function?')
        
        ''' Make sure we logged an error message to the device log 
            if the error message is not found in the list, the ".index" method will throw a value error '''
        if(len(mock_catalyst.log_messages) > 0):  
            try:  
                mock_catalyst.log_messages.index(\
                            'Button "BUTTON-DOES-NOT-EXIST" was not found for instruction "GetNumeric" for screen id "RLMENU888-1"')
            except ValueError:
                self.fail('Did not find the expected error message in the log file.')
        else:
            self.fail('Did not find the expected error message in the log file.')

    def test_nofieldvalue_post_button_error_ready_spoken(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3ODJlZjQ5SlEwNXpYT0JrOHM","tOTFxa3pyQXNZZnF1dTZGLUFUVA==)/vowm_lm01/~flNUQVRFPTEyOTUwLjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3ODJlZjQ5SlEwNXpYT0JrOHM","tOTFxa3pyQXNZZnF1dTZGLUFUVA==)/vowm_lm01/~flNUQVRFPTc5NDAuMDAzLjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3ODJlZjQ5SlEwNXpYT0JrOHM","tOTFxa3pyQXNZZnF1dTZGLUFUVA==)/vowm_lm01/~flNUQVRFPTczMjMuMDA0LjAyLjAy====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3ODJlZjQ5SlEwNXpYT0JrOHM","tOTFxa3pyQXNZZnF1dTZGLUFUVA==)/vowm_lm01/~flNUQVRFPTEwMDMwLjAwNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","2","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PPSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PPGDN","~OKCode","PGDN","1","7","vcommand007.next.slot","","","","","","","","v","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',      # Password?
                                   '2!',           # Function?
                                   '1!',           # Work type?
                                   '11306!',       # Transfer Order
                                   'VRESERVE001',  # Error in Voice Attributes file. Please see your device log, to continue, say ready.
                                   '-')            # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Work type?',
                              'Transfer Order',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?',
                              'Error in Voice Attributes file. Please see your device log, to continue, say ready.')
                              

        
        #validate log messages
        if(len(mock_catalyst.log_messages) > 0):  
            try:  
                mock_catalyst.log_messages.index(\
                            'Button "RLMOB-PPSAVE" was not found for instruction "GetNumeric" for screen id "SAPLLMOB212"')
            except ValueError:
                self.fail('Did not find the expected error message in the log file.')
        else:
            self.fail('Did not find the expected error message in the log file.')

    def test_nofieldvalue_post_button_error_value_spoken(self):
        #queue of LUT responses
        self.set_server_response('"ScreenID","PT-INIT-Integrated","","PT-INIT-Integrated","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"Help","HELP","","","1","0","","say ready.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","WelcomePrompt","","","1","1","","","Welcome to the Voice Direct ERP system.","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SpeakPrompt","OperatorPrompt","",".operator","1","2","","","Current operator is ",", to continue, say ready.","","","","","","","0","0","0","1","1","0","0","0","",0\r\n'
                                 '"Help","HELP","","","2","0","","please say your password.","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-user","sap-user",".operatorId","2","1","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-client","sap-client","800","2","2","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"PassThrough","sap-language","sap-language",".languageCode","2","3","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"GetNumeric","sap-Password","sap-Password","","2","4","","","Password?","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '"SignOn","SignOn","","","2","5","","","","","","","","","","","0","0","0","0","0","0","0","0","",0\r\n'
                                 '\n'
                                 '\n')
        
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1VHplRXc2d0N2N0hIMzNGS25","MYjFxa3pyS3NZYzZmRlJYLUFUVA==)/vowm_lm01/~flNUQVRFPTIyODM0LjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1VHplRXc2d0N2N0hIMzNGS25","MYjFxa3pyS3NZYzZmRlJYLUFUVA==)/vowm_lm01/~flNUQVRFPTI3NjI2LjAwMy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1VHplRXc2d0N2N0hIMzNGS25","MYjFxa3pyS3NZYzZmRlJYLUFUVA==)/vowm_lm01/~flNUQVRFPTQyNzEuMDA0LjAyLjAy====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PPNEXT","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1VHplRXc2d0N2N0hIMzNGS25","MYjFxa3pyS3NZYzZmRlJYLUFUVA==)/vowm_lm01/~flNUQVRFPTIyMDg0LjAwNC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PPNEXT","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","ENDOFSESSION","","ENDOFSESSION","0","0","","http://10.0.13.76:8006/sap/vowm_lm01/","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","ENDOFSESSION","","ENDOFSESSION","1","1","","","sign.off.message","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
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

        #queue of Dialog Responses
        self.post_dialog_responses('VRESERVE001',  # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',      # Password?
                                   '2!',           # Function?
                                   '1!',           # Work type?
                                   '11306!',       # Transfer Order
                                   'VRESERVE001',  # Error in Voice Attributes file. Please see your device log, to continue, say ready.
                                   'VRESERVE002',  # Transfer Order
                                   'VRESERVE003',  # VRESERVE002, correct?
                                   '-')            # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Work type?',
                              'Transfer Order',
                              'Error in Voice Attributes file. Please see your device log, to continue, say ready.',
                              'Transfer Order',
                              'VRESERVE002, correct?',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.')
        
        if(len(mock_catalyst.log_messages) > 0):  
            try:  
                mock_catalyst.log_messages.index(\
                            'Button "RLMOB-PPNEXT" was not found for instruction "GetNumeric" for screen id "SAPLLMOB100"')
            except ValueError:
                self.fail('Did not find the expected error message in the log file.')
        else:
            self.fail('Did not find the expected error message in the log file.')

    def test_button_error_speak_prompt(self):
                
        ''' The purpose of this test is to verify that we throw a "Error in voice attributes" message back to the user
            if they mis-spell the button ID in a "Speak Prompt command".  '''
        
        pass
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()