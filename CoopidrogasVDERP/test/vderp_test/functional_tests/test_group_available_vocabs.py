#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
# Verify that the correct vocabulary words are available based on the group number
from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, \
    BOTH_SERVERS #Needs to be first import
from main import main
import unittest

class testGroupAvailableVocabs(BaseVDERPTestCase):
    '''
    Verify that the correct vocabulary words are available based on the group number
    '''

    def setUp(self):
        self.start_server(BOTH_SERVERS)
        self.clear()

    def testGroupAvailableVocabs(self):
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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTIyMjcuMDAyLjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTI3MTY0LjAwMy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzMxLjAwNC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE4MjM4LjAwNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","2","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","2","2","vcommand012.storage.location","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","2","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","2","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","2","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","2","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PPGDN","~OKCode","PGDN","2","7","vcommand007.next.slot","","","","","","","","v","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","2","11","vcommand015.detail","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","2","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","2","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","2","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","2","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB221","","SAPLLMOB221","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE3ODUzLjAwNi4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15026","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-CHARG","ltap-charg[1]","0080009080","1","12","vcommand004.batch","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE1Nzg2LjAwNy4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","1","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","2","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","2","2","vcommand012.storage.location","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","2","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","2","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","2","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","2","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PPGDN","~OKCode","PGDN","2","7","vcommand007.next.slot","","","","","","","","v","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","2","11","vcommand015.detail","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","2","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","2","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","2","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","2","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTg3NzEuMDA4LjAyLjAy====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
        self.post_dialog_responses('VRESERVE001',   # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.
                                   '123456!',          # Password?
                                   '2!',            # Function?
                                   '1!',            # Work type?
                                   '15026!',        # Transfer Order
                                   'VCOMMAND012',   # storage type VWO ,,
                                   'VCOMMAND015',   # storage type VWO ,,
                                   'VCOMMAND003',   # storage type VWO ,,
                                   'VRESERVE001',   # storage type VWO ,,
                                   'talkman help',  # source bin VO-01-01 ,,
                                   'VCOMMAND012',   # source bin VO-01-01 ,,
                                   'VCOMMAND002',   # source bin VO-01-01 ,,
                                   'VCOMMAND003',   # source bin VO-01-01 ,,
                                   'VCOMMAND015',   # source bin VO-01-01 ,,
                                   'VRESERVE001',   # source bin VO-01-01 ,,
                                   'talkman help',  # pick 2 eaches ,, check digit?
                                   'VCOMMAND012',   # pick 2 eaches ,, check digit?
                                   'VCOMMAND002',   # pick 2 eaches ,, check digit?
                                   'VCOMMAND003',   # pick 2 eaches ,, check digit?
                                   'VCOMMAND015',   # pick 2 eaches ,, check digit?
                                   'talkman help',  # which detail??
                                   'VCOMMAND002',   # which detail??
                                   'VCOMMAND003',   # which detail??
                                   'VCOMMAND010',   # which detail??
                                   'VCOMMAND011',   # which detail??
                                   'VCOMMAND012',   # which detail??
                                   'VCOMMAND013',   # which detail??
                                   'VCOMMAND014',   # which detail??
                                   'VCOMMAND004',   # which detail??
                                   'VRESERVE001',   # which detail??
                                   'VCOMMAND018',   # storage type VWO ,,
                                   'VRESERVE002',   # Transfer Order
                                   'VRESERVE003',   # VRESERVE002, correct?
                                   '-')             # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Work type?',
                              'Transfer Order',
                              'storage type VWO ,,',
                              'source bin VO-01-01 ,,',
                              'Speak the check digits, or say VCOMMAND018',
                              'source bin VO-01-01 ,,',
                              'pick 1 eaches ,, check digit?',
                              'Speak the check digits, or say VCOMMAND012, VCOMMAND002, VCOMMAND003, VCOMMAND016, VCOMMAND015, VCOMMAND007,  or VCOMMAND018',
                              'pick 1 eaches ,, check digit?',
                              'VO-01-01',
                              'pick 1 eaches ,, check digit?',
                              'VW_MAT3',
                              'pick 1 eaches ,, check digit?',
                              'Material 3',
                              'pick 1 eaches ,, check digit?',
                              'which detail?',
                              'say ready. or say VCOMMAND011, VCOMMAND013, VCOMMAND012, VCOMMAND002, VCOMMAND003, VCOMMAND004, VCOMMAND010,  or VCOMMAND014',
                              'which detail?',
                              'VW_MAT3',
                              'which detail?',
                              'Material 3',
                              'which detail?',
                              'VW1',
                              'which detail?',
                              'VW01',
                              'which detail?',
                              'VW01',
                              'which detail?',
                              '15026',
                              'which detail?',
                              '1',
                              'which detail?',
                              '0080009080',
                              'which detail?',
                              'storage type VWO ,,',
                              'Transfer Order',
                              'VRESERVE002, correct?',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.')

        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTIyMjcuMDAyLjAxLjAx===="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTI3MTY0LjAwMy4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzMxLjAwNC4wMi4wMg=="', '""', '"~OKCode"', '"NEXT"', '"inp_100[1]"', '"15026"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE4MjM4LjAwNS4wMy4wNA=="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE3ODUzLjAwNi4wNC4wNQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTE1Nzg2LjAwNy4wMy4wNA=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"SignOff"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc1TUM3ZnJuV1Bna1M4Y1hrWnBiTzVxa3pycXRZZk5LZ01YLUFUVA==)/vowm_lm01/~flNUQVRFPTg3NzEuMDA4LjAyLjAy===="', '""', '"~OKCode"', '"/NEX"'],
                                      ['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])
        #validate log messages

if __name__ == '__main__':
    unittest.main()
