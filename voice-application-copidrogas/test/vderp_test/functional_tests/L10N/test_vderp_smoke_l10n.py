#!/usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
# PyUnit version of LM05 transaction smoke test.
from BaseVDERPTestCase import BaseVDERPTestCase, EndOfApplication, BOTH_SERVERS #Needs to be first import
from main import main
import unittest
import mock_catalyst




class test_vderp_smoke(BaseVDERPTestCase):
    '''
    Test screens, help commands and vocabulary for LM05 pick by Transfer Order transaction
    '''
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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1NDAzLjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE4NjI2LjAwMy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTM3MDAuMDA0LjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNTExLjAwNS4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MjI4LjAwNi4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEzODAwLjAwNy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTI1LjAwOC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transfer Order","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2NDM0LjAwOS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4NzU0LjAxMC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PPGUP","~OKCode","PGUP","1","8","vcommand008.previous.slot","","","","","","","","^","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTY1NDQuMDExLjAzLjA0====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2MjA3LjAxMi4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB221","","SAPLLMOB221","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIxNTQ5LjAxMy4wNS4wNg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-CHARG","ltap-charg[1]","0080009094","1","12","vcommand004.batch","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNzg3LjAxNC4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI3ODg4LjAxNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB221","","SAPLLMOB221","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MzAyLjAxNi4wNS4wNg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-CHARG","ltap-charg[1]","0080009094","1","12","vcommand004.batch","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzOTYxLjAxNy4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTk2NjkuMDE4LjAzLjA0====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI5ODU1LjAxOS4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE1OTc5LjAyMC4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTYxMzYuMDIxLjA2LjA4====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB321","","SAPLLMOB321","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2NjcxLjAyMi4wNy4wOQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2MDAxLjAyMy4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzNDc3LjAyNC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIyODIxLjAyNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTMyMzE2LjAyNi4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTkwLjAyNy4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4OTExLjAyOC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzguMDI5LjA2LjA4====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEyNjM3LjAzMC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
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
                                   'talkman help',  # Function?
                                   'VRESERVE005',   # Function?
                                   'VRESERVE001',   # 1, Put away
                                   'VRESERVE001',   # 2, Picking
                                   'VRESERVE001',   # 3, Inventory
                                   'VRESERVE005',   # Function?
                                   'VRESERVE006',   # 1, Put away
                                   'VRESERVE002',   # Function?
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '2!',            # Function?
                                   'talkman help',  # Work type?
                                   'VCOMMAND001',   # Work type?
                                   'VRESERVE004',   # VCOMMAND001, correct?
                                   'VCOMMAND001',   # Work type?
                                   'VRESERVE003',   # VCOMMAND001, correct?
                                   '2!',            # Function?
                                   'VRESERVE005',   # Work type?
                                   'VRESERVE001',   # 1, Pick by transfer order.
                                   'VRESERVE001',   # 2, Pick and pack
                                   'VRESERVE005',   # Work type?
                                   'VRESERVE006',   # 1, Pick by transfer order.
                                   'VRESERVE002',   # Work type?
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '1!',            # Work type?
                                   'talkman help',  # Transfer Order
                                   'VCOMMAND009',   # Transfer Order
                                   'VRESERVE004',   # VCOMMAND009, correct?
                                   'VCOMMAND009',   # Transfer Order
                                   'VRESERVE003',   # VCOMMAND009, correct?
                                   '1!',            # Work type?
                                   'VRESERVE002',   # Transfer Order
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '15050!',        # Transfer Order
                                   'talkman help',  # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND007',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND008',   # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, check digit?
                                   'VCOMMAND002',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND003',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND016',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'talkman help',  # quantity?
                                   'VCOMMAND002',   # quantity?
                                   'VCOMMAND003',   # quantity?
                                   'VCOMMAND013',   # quantity?
                                   'VCOMMAND014',   # quantity?
                                   'VCOMMAND015',   # quantity?
                                   'VRESERVE001',   # which detail?
                                   'VCOMMAND018',   # quantity?
                                   'VCOMMAND015',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'talkman help',  # which detail?
                                   'VCOMMAND002',   # which detail?
                                   'VCOMMAND003',   # which detail?
                                   'VCOMMAND010',   # which detail?
                                   'VCOMMAND011',   # which detail?
                                   'VCOMMAND012',   # which detail?
                                   'VCOMMAND013',   # which detail?
                                   'VCOMMAND014',   # which detail?
                                   'VCOMMAND004',   # which detail?
                                   'VRESERVE001',   # which detail?
                                   '123!',          # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, confirmed.
                                   'talkman help',  # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND002',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND003',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND016',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND018',   # quantity?
                                   'VCOMMAND015',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'talkman help',  # which detail?
                                   'VCOMMAND002',   # which detail?
                                   'VCOMMAND003',   # which detail?
                                   'VCOMMAND010',   # which detail?
                                   'VCOMMAND011',   # which detail?
                                   'VCOMMAND012',   # which detail?
                                   'VCOMMAND013',   # which detail?
                                   'VCOMMAND014',   # which detail?
                                   'VCOMMAND004',   # which detail?
                                   'VRESERVE001',   # which detail?
                                   'VCOMMAND018',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   '123!',          # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, confirmed.
                                   'VRESERVE001',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   '123!',          # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, confirmed.
                                   'VRESERVE001',   # destination storage type 916 , destination bin 0080006512 ,, put 4 eaches to deliver, say ready
                                   'VRESERVE002',   # Transfer Order
                                   'VRESERVE003',   # VRESERVE002, correct?
                                   '-')             # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.

        #run main application
        self.assertRaises(EndOfApplication, main)

        #validate prompts
        self.validate_prompts('Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.',
                              'Password?',
                              'Function?',
                              'Speak the function number, or say VRESERVE005,  or VRESERVE002',
                              'Function?',
                              '1, Put away',
                              '2, Picking',
                              '3, Inventory',
                              'Function?',
                              '1, Put away',
                              'Function?',
                              'VRESERVE002, correct?',
                              'Function?',
                              'Work type?',
                              'Speak the work type number, or say VRESERVE005, VCOMMAND001,  or VRESERVE002',
                              'Work type?',
                              'VCOMMAND001, correct?',
                              'Work type?',
                              'VCOMMAND001, correct?',
                              'Function?',
                              'Work type?',
                              '1, Pick by transfer order.',
                              '2, Pick and pack',
                              'Work type?',
                              '1, Pick by transfer order.',
                              'Work type?',
                              'VRESERVE002, correct?',
                              'Work type?',
                              'Transfer Order',
                              'Speak the transfer order number, or say VCOMMAND009,  or VRESERVE002',
                              'Transfer Order',
                              'VCOMMAND009, correct?',
                              'Transfer Order',
                              'VCOMMAND009, correct?',
                              'Work type?',
                              'Transfer Order',
                              'VRESERVE002, correct?',
                              'Transfer Order',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'Speak the check digits, or say VCOMMAND002, VCOMMAND003, VCOMMAND017, VCOMMAND016, VCOMMAND015, VCOMMAND007,  or VCOMMAND018',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'storage type VWO ,, source bin VO-04-06 ,, pick 1 eaches ,, check digit?',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'VW_MAT3',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'Material 3',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'quantity?',
                              'Speak the quantity, or say VCOMMAND013, VCOMMAND002, VCOMMAND003, VCOMMAND015, VCOMMAND014,  or VCOMMAND018',
                              'quantity?',
                              'VW_MAT3',
                              'quantity?',
                              'Material 3',
                              'quantity?',
                              '15050',
                              'quantity?',
                              '1',
                              'quantity?',
                              'which detail?',
                              'quantity?',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
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
                              '15050',
                              'which detail?',
                              '1',
                              'which detail?',
                              '0080009094',
                              'which detail?',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, confirmed.',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'say ready. or say VCOMMAND002, VCOMMAND003, VRESERVE001, VCOMMAND016, VCOMMAND015,  or VCOMMAND018',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'VW_MAT3',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'Material 3',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'quantity?',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'which detail?',
                              'say ready. or say VCOMMAND011, VCOMMAND013, VCOMMAND012, VCOMMAND002, VCOMMAND003, VCOMMAND010,  or VCOMMAND014',
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
                              '15050',
                              'which detail?',
                              '1',
                              'which detail?',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, check digit?',
                              'storage type VWO ,, source bin VO-01-01 ,, pick 1 eaches ,, confirmed.',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'storage type VWO ,, source bin VO-04-06 ,, pick 1 eaches ,, check digit?',
                              'storage type VWO ,, source bin VO-04-06 ,, pick 1 eaches ,, confirmed.',
                              'destination,,, storage type 916 ,, bin 0080009094 ,, put items,,, ,, to deliver, say ready',
                              'Transfer Order',
                              'VRESERVE002, correct?',
                              'Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.')

        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"en_US"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"EN"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1NDAzLjAwMi4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE4NjI2LjAwMy4wMS4wMQ=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTM3MDAuMDA0LjAxLjAx===="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNTExLjAwNS4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MjI4LjAwNi4wMi4wMg=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEzODAwLjAwNy4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTI1LjAwOC4wMi4wMg=="', '""', '"~OKCode"', '"NEXT"', '"inp_100[1]"', '"15050"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2NDM0LjAwOS4wMy4wNA=="', '""', '"~OKCode"', '"PGDN"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4NzU0LjAxMC4wMy4wNA=="', '""', '"~OKCode"', '"PGUP"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTY1NDQuMDExLjAzLjA0===="', '""', '"~OKCode"', '"DIFF"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2MjA3LjAxMi4wNC4wNQ=="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIxNTQ5LjAxMy4wNS4wNg=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNzg3LjAxNC4wNC4wNQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI3ODg4LjAxNS4wMy4wNA=="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MzAyLjAxNi4wNS4wNg=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzOTYxLjAxNy4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTk2NjkuMDE4LjAzLjA0===="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI5ODU1LjAxOS4wNi4wOA=="', '""', '"~OKCode"', '"DIFF"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE1OTc5LjAyMC4wNC4wNQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTYxMzYuMDIxLjA2LjA4===="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2NjcxLjAyMi4wNy4wOQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2MDAxLjAyMy4wNi4wOA=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzNDc3LjAyNC4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIyODIxLjAyNS4wMy4wNA=="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTMyMzE2LjAyNi4wNi4wOA=="', '""', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTkwLjAyNy4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4OTExLjAyOC4wMy4wNA=="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzguMDI5LjA2LjA4===="', '""', '"~OKCode"', '"SAVE"'],
                                      ['"SignOff"', '"en_US"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEyNjM3LjAzMC4wMi4wMg=="', '""', '"~OKCode"', '"/NEX"'],
                                      ['"Init"', '"en_US"', '""', '""', '""', '""', '""', '""'])
        #validate log messages



###################


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
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1NDAzLjAwMi4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE4NjI2LjAwMy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-1","","RLMENU888-1","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTM3MDAuMDA0LjAxLjAx====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","2","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","function.number.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","1","","","","","","","","","1.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","2","","","","","","","","","2.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT3","~OKCode","3","1","3","","","","","","","","","3.main.voc.menu                      >","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","8","","","function.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","9","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNTExLjAwNS4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MjI4LjAwNi4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transportauftrag","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","RLMENU888-2","","RLMENU888-2","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEzODAwLjAwNy4wMS4wMQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","work.type.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","1","1","vreserve002.sign.off","","","","","","","correct.message","F8 LOff","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","2","vcommand001.new.function","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","TEXT1","~OKCode","1","1","3","","","","","","","","","1.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"Button","TEXT2","~OKCode","2","1","4","","","","","","","","","2.picking.voc.menu                 ...","","0","0","0","0","0","1","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-MENOPT","rlmob-menopt[1]","","1","9","","","work.type.prompt","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","10","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTI1LjAwOC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transportauftrag","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand009.new.work.type","","","","","","","correct.message","F3 Back","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","NEXT","1","7","","","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2NDM0LjAwOS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4NzU0LjAxMC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PPGUP","~OKCode","PGUP","1","8","vcommand008.previous.slot","","","","","","","","^","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTY1NDQuMDExLjAzLjA0====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2MjA3LjAxMi4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB221","","SAPLLMOB221","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIxNTQ5LjAxMy4wNS4wNg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-CHARG","ltap-charg[1]","0080009094","1","12","vcommand004.batch","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNzg3LjAxNC4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI3ODg4LjAxNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB221","","SAPLLMOB221","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MzAyLjAxNi4wNS4wNg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-CHARG","ltap-charg[1]","0080009094","1","12","vcommand004.batch","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzOTYxLjAxNy4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTk2NjkuMDE4LjAzLjA0====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI5ODU1LjAxOS4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB400","","SAPLLMOB400","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE1OTc5LjAyMC4wNC4wNQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","quantity.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","RLMOB-CQTY","rlmob-cqty[1]","1","1","2","","","quantity.prompt","","","","","","","RLMOB-PCONF","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","3","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","4","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","5","vcommand013.to.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","6","vcommand014.to.item","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PCONF","~OKCode","CONF","1","7","","","","","","","","","F1 Conf","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/ECANC","1","8","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","9","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTYxMzYuMDIxLjA2LjA4====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB321","","SAPLLMOB321","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2NjcxLjAyMi4wNy4wOQ==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","DETAIL-PROMPT","","","1","1","","","","","","","","","","RLMOB-POK","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-POK","~OKCode","/ECANC","1","2","","which.detail.prompt","","","","","","","OK","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","5","vcommand002.material.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","6","vcommand003.material.description","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGNUM","ltap-lgnum[1]","VW1","1","7","vcommand010.warehouse","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-WERKS","ltap-werks[1]","VW01","1","8","vcommand011.plant","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-LGORT","ltap-lgort[1]","VW01","1","9","vcommand012.storage.location","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TANUM","ltap-tanum[1]","15050","1","10","vcommand013.to.number","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-TAPOS","ltap-tapos[1]","1","1","11","vcommand014.to.item","","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2MDAxLjAyMy4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzNDc3LjAyNC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIyODIxLjAyNS4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-01-01","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTMyMzE2LjAyNi4wNi4wOA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT3","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 3","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTkwLjAyNy4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"GetNumeric","RLMOB-CLGPLA","rlmob-clgpla[1]","123","1","5","","","check.digit2.prompt","","wrong.message","try.again.message","","","","RLMOB-PSAVE","1","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB212","","SAPLLMOB212","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4OTExLjAyOC4wMy4wNA==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","speak.check.digits.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLTYP","ltap-vltyp[1]","VWO","1","1","","","storage.type.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-VLPLA","ltap-vlpla[1]","VO-04-06","1","2","","","source.bin.message",",,","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-VSOLA","rlmob-vsola[1]","1","1","3","","","pick.message","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-ALTME","ltap-altme[1]","EA","1","4","","","",",,","","","","","","","0","0","0","1","0","0","0","0","","1"\r\n'
                                 '"SpeakPrompt","LTAP-KZQUI","ltap-kzqui[1]","X","1","6","","","","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","7","","","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","10","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PNEXT","~OKCode","CMPL","1","11","vcommand017.deliver","confirmed.message","","","","","","","F4 Nxt","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","12","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","16","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","17","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB312","","SAPLLMOB312","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzguMDI5LjA2LjA4====","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","0","","say.ready.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLTYP","ltap-nltyp[1]","916","1","1","","","destination.storage.type.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","LTAP-NLPLA","ltap-nlpla[1]","0080009094","1","2","","","destination.bin.message",",,","","","","","","RLMOB-PSAVE","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"SpeakPrompt","RLMOB-NSOLA","rlmob-nsola[1]","1","1","3","","","put.message","","","","","","","RLMOB-PSAVE","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PSAVE","~OKCode","SAVE","1","5","vreserve001.ready","deliver.say.ready.message","","","","","","","F1 Save","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PBACK","~OKCode","/EBACK","1","6","vcommand018.back","","","","","","","","F3 Back","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDIFF","~OKCode","DIFF","1","10","vcommand016.difference","","","","","","","","F6 Diff","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PDETL","~OKCode","DETL","1","11","vcommand015.detail","","","","","","","","F5 Det","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","LTAP-MATNR","ltap-matnr[1]","VW_MAT4","1","15","vcommand002.material.number","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '"Vocabulary","RLMOB-MMAKT","rlmob-mmakt[1]","Material 4","1","16","vcommand003.material.description","","","","","","","","","","0","0","0","1","0","0","0","0","","0"\r\n'
                                 '\n'
                                 '\n')
        self.set_server_response('"ScreenID","SAPLLMOB100","","SAPLLMOB100","0","0","","http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEyNjM3LjAzMC4wMi4wMg==","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"Button","RLMOB-PMLGF","~OKCode","/NEX","0","1","vreserve002.sign.off","","","","","","","correct.message","","","0","0","1","0","0","0","0","0","","0"\r\n'
                                 '"Help","HELP","","","1","1","","transfer.order.message","","","","","","","","","0","0","0","0","0","0","0","0","","0"\r\n'
                                 '"GetNumeric","INP_100","inp_100[1]","","1","2","","","Transportauftrag","","","","","","","RLMOB-PNEXT","0","0","0","0","0","0","0","0","","0"\r\n'
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
                                   'talkman help',  # Function?
                                   'VRESERVE005',   # Function?
                                   'VRESERVE001',   # 1, Put away
                                   'VRESERVE001',   # 2, Picking
                                   'VRESERVE001',   # 3, Inventory
                                   'VRESERVE005',   # Function?
                                   'VRESERVE006',   # 1, Put away
                                   'VRESERVE002',   # Function?
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '2!',            # Function?
                                   'talkman help',  # Work type?
                                   'VCOMMAND001',   # Work type?
                                   'VRESERVE004',   # VCOMMAND001, correct?
                                   'VCOMMAND001',   # Work type?
                                   'VRESERVE003',   # VCOMMAND001, correct?
                                   '2!',            # Function?
                                   'VRESERVE005',   # Work type?
                                   'VRESERVE001',   # 1, Pick by transfer order.
                                   'VRESERVE001',   # 2, Pick and pack
                                   'VRESERVE005',   # Work type?
                                   'VRESERVE006',   # 1, Pick by transfer order.
                                   'VRESERVE002',   # Work type?
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '1!',            # Work type?
                                   'talkman help',  # Transfer Order
                                   'VCOMMAND009',   # Transfer Order
                                   'VRESERVE004',   # VCOMMAND009, correct?
                                   'VCOMMAND009',   # Transfer Order
                                   'VRESERVE003',   # VCOMMAND009, correct?
                                   '1!',            # Work type?
                                   'VRESERVE002',   # Transfer Order
                                   'VRESERVE004',   # VRESERVE002, correct?
                                   '15050!',        # Transfer Order
                                   'talkman help',  # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND007',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND008',   # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, check digit?
                                   'VCOMMAND002',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND003',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND016',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'talkman help',  # quantity?
                                   'VCOMMAND002',   # quantity?
                                   'VCOMMAND003',   # quantity?
                                   'VCOMMAND013',   # quantity?
                                   'VCOMMAND014',   # quantity?
                                   'VCOMMAND015',   # quantity?
                                   'VRESERVE001',   # which detail?
                                   'VCOMMAND018',   # quantity?
                                   'VCOMMAND015',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'talkman help',  # which detail?
                                   'VCOMMAND002',   # which detail?
                                   'VCOMMAND003',   # which detail?
                                   'VCOMMAND010',   # which detail?
                                   'VCOMMAND011',   # which detail?
                                   'VCOMMAND012',   # which detail?
                                   'VCOMMAND013',   # which detail?
                                   'VCOMMAND014',   # which detail?
                                   'VCOMMAND004',   # which detail?
                                   'VRESERVE001',   # which detail?
                                   '123!',          # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, confirmed.
                                   'talkman help',  # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND002',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND003',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND016',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'VCOMMAND018',   # quantity?
                                   'VCOMMAND015',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   'talkman help',  # which detail?
                                   'VCOMMAND002',   # which detail?
                                   'VCOMMAND003',   # which detail?
                                   'VCOMMAND010',   # which detail?
                                   'VCOMMAND011',   # which detail?
                                   'VCOMMAND012',   # which detail?
                                   'VCOMMAND013',   # which detail?
                                   'VCOMMAND014',   # which detail?
                                   'VCOMMAND004',   # which detail?
                                   'VRESERVE001',   # which detail?
                                   'VCOMMAND018',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   '123!',          # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-01-01 ,, pick 2 eaches ,, confirmed.
                                   'VRESERVE001',   # destination storage type 916 , destination bin 0080006512 ,, put 2 eaches to deliver, say ready
                                   '123!',          # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, check digit?
                                   'VCOMMAND017',   # storage type VWO ,, source bin VO-04-06 ,, pick 4 eaches ,, confirmed.
                                   'VRESERVE001',   # destination storage type 916 , destination bin 0080006512 ,, put 4 eaches to deliver, say ready
                                   'VRESERVE002',   # Transfer Order
                                   'VRESERVE003',   # VRESERVE002, correct?
                                   '-')             # Welcome to the Voice Direct ERP system. Current operator is Operator.Name , to continue, say ready.


        #run main application
        self.assertRaises(EndOfApplication, main)




        #validate prompts
        self.validate_prompts('Willkommen beim Voice Direct ERP System. Aktueller Benutzer ist Operator.Name , Um fortzufahren, sagen Sie bereit.',
                              'Passwort?',
                              'Funktion?',
                              'Sagen Sie die Funktionszahl oder sagen Sie folgendes, oder Sagen Sie VRESERVE005,  oder VRESERVE002',
                              'Funktion?',
                              '1, Einlagern',
                              '2, Kommissionieren',
                              '3, Warenbestand',
                              'Funktion?',
                              '1, Einlagern',
                              'Funktion?',
                              'VRESERVE002, korrigieren?',
                              'Funktion?',
                              'taetigkeit wechseln?',
                              'Sagen Sie die Tätigkeitszahl oder sagen Sie folgendes, oder Sagen Sie VRESERVE005, VCOMMAND001,  oder VRESERVE002',
                              'taetigkeit wechseln?',
                              'VCOMMAND001, korrigieren?',
                              'taetigkeit wechseln?',
                              'VCOMMAND001, korrigieren?',
                              'Funktion?',
                              'taetigkeit wechseln?',
                              '1, Auslagerung nach TA-Nummer',
                              '2, Kommissionieren und packen',
                              'taetigkeit wechseln?',
                              '1, Auslagerung nach TA-Nummer',
                              'taetigkeit wechseln?',
                              'VRESERVE002, korrigieren?',
                              'taetigkeit wechseln?',
                              'Transportauftrag',
                              'Sagen sie die Transportauftragsnummer oder sagen Sie folgendes, oder Sagen Sie VCOMMAND009,  oder VRESERVE002',
                              'Transportauftrag',
                              'VCOMMAND009, korrigieren?',
                              'Transportauftrag',
                              'VCOMMAND009, korrigieren?',
                              'taetigkeit wechseln?',
                              'Transportauftrag',
                              'VRESERVE002, korrigieren?',
                              'Transportauftrag',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'Sprechen Sie die Prüfziffer oder sagen Sie folgendes, oder Sagen Sie VCOMMAND002, VCOMMAND003, VCOMMAND017, VCOMMAND016, VCOMMAND015, VCOMMAND007,  oder VCOMMAND018',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'lagerart VWO ,, quellfach VO-04-06 ,, nimm 1 Stück ,, prüfziffer?',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'VW_MAT3',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'Material 3',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'menge?',
                              'Sagen Sie die Menge oder sagen Sie folgendes, oder Sagen Sie VCOMMAND013, VCOMMAND002, VCOMMAND003, VCOMMAND015, VCOMMAND014,  oder VCOMMAND018',
                              'menge?',
                              'VW_MAT3',
                              'menge?',
                              'Material 3',
                              'menge?',
                              '15050',
                              'menge?',
                              '1',
                              'menge?',
                              'welches detail?',
                              'menge?',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'welches detail?',
                              'Sagen Sie Bereit. oder Sagen Sie VCOMMAND011, VCOMMAND013, VCOMMAND012, VCOMMAND002, VCOMMAND003, VCOMMAND004, VCOMMAND010,  oder VCOMMAND014',
                              'welches detail?',
                              'VW_MAT3',
                              'welches detail?',
                              'Material 3',
                              'welches detail?',
                              'VW1',
                              'welches detail?',
                              'VW01',
                              'welches detail?',
                              'VW01',
                              'welches detail?',
                              '15050',
                              'welches detail?',
                              '1',
                              'welches detail?',
                              '0080009094',
                              'welches detail?',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, bestätigt.',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'Sagen Sie Bereit. oder Sagen Sie VCOMMAND002, VCOMMAND003, VRESERVE001, VCOMMAND016, VCOMMAND015,  oder VCOMMAND018',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'VW_MAT3',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'Material 3',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'menge?',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'welches detail?',
                              'Sagen Sie Bereit. oder Sagen Sie VCOMMAND011, VCOMMAND013, VCOMMAND012, VCOMMAND002, VCOMMAND003, VCOMMAND010,  oder VCOMMAND014',
                              'welches detail?',
                              'VW_MAT3',
                              'welches detail?',
                              'Material 3',
                              'welches detail?',
                              'VW1',
                              'welches detail?',
                              'VW01',
                              'welches detail?',
                              'VW01',
                              'welches detail?',
                              '15050',
                              'welches detail?',
                              '1',
                              'welches detail?',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, prüfziffer?',
                              'lagerart VWO ,, quellfach VO-01-01 ,, nimm 1 Stück ,, bestätigt.',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'lagerart VWO ,, quellfach VO-04-06 ,, nimm 1 Stück ,, prüfziffer?',
                              'lagerart VWO ,, quellfach VO-04-06 ,, nimm 1 Stück ,, bestätigt.',
                              'ziellagerart 916 ,, zielbehälter 0080009094 ,, legen um zu liefern, sagen Sie bereit',
                              'Transportauftrag',
                              'VRESERVE002, korrigieren?',
                              'Willkommen beim Voice Direct ERP System. Aktueller Benutzer ist Operator.Name , Um fortzufahren, sagen Sie bereit.')





        #validate LUT Requests
        self.validate_server_requests(['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'],
                                      ['"SignOn"', '"de_DE"', '"http://10.0.13.76:8006/sap/vowm_lm01/"', '""', '"sap-client"', '"800"', '"sap-user"', '"Operator.Id"', '"sap-Password"', '"123456"', '"sap-language"', '"DE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1NDAzLjAwMi4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE4NjI2LjAwMy4wMS4wMQ=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTM3MDAuMDA0LjAxLjAx===="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"2"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNTExLjAwNS4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MjI4LjAwNi4wMi4wMg=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEzODAwLjAwNy4wMS4wMQ=="', '""', '"~OKCode"', '"NEXT"', '"rlmob-menopt[1]"', '"1"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTI1LjAwOC4wMi4wMg=="', '""', '"~OKCode"', '"NEXT"', '"inp_100[1]"', '"15050"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2NDM0LjAwOS4wMy4wNA=="', '""', '"~OKCode"', '"PGDN"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4NzU0LjAxMC4wMy4wNA=="', '""', '"~OKCode"', '"PGUP"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTY1NDQuMDExLjAzLjA0===="', '""', '"~OKCode"', '"DIFF"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2MjA3LjAxMi4wNC4wNQ=="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIxNTQ5LjAxMy4wNS4wNg=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwNzg3LjAxNC4wNC4wNQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI3ODg4LjAxNS4wMy4wNA=="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI1MzAyLjAxNi4wNS4wNg=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzOTYxLjAxNy4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTk2NjkuMDE4LjAzLjA0===="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI5ODU1LjAxOS4wNi4wOA=="', '""', '"~OKCode"', '"DIFF"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE1OTc5LjAyMC4wNC4wNQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTYxMzYuMDIxLjA2LjA4===="', '""', '"~OKCode"', '"DETL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTE2NjcxLjAyMi4wNy4wOQ=="', '""', '"~OKCode"', '"/ECANC"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI2MDAxLjAyMy4wNi4wOA=="', '""', '"~OKCode"', '"/EBACK"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIzNDc3LjAyNC4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIyODIxLjAyNS4wMy4wNA=="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTMyMzE2LjAyNi4wNi4wOA=="', '""', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEwNTkwLjAyNy4wMy4wNA=="', '""', '"rlmob-clgpla[1]"', '"123"', '"~OKCode"', '"SAVE"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTI4OTExLjAyOC4wMy4wNA=="', '""', '"~OKCode"', '"CMPL"'],
                                      ['"Post"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTIwMzguMDI5LjA2LjA4===="', '""', '"~OKCode"', '"SAVE"'],
                                      ['"SignOff"', '"de_DE"', '"http://10.0.13.76:8006/sap(cz1TSUQlM2FBTk9OJTNhc3FhLXNhcC1idWlsZF9FQzFfMDYlM2FqRlN6SXc3QUxqd1BYY0NKbEVNUjhPa3A4X2hxa3pvTXVvZW43bnlJLUFUVA==)/vowm_lm01/~flNUQVRFPTEyNjM3LjAzMC4wMi4wMg=="', '""', '"~OKCode"', '"/NEX"'],
                                      ['"Init"', '"de_DE"', '""', '""', '""', '""', '""', '""'])
   


if __name__ == '__main__':
    unittest.main()
