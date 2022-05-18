'''
Created on Apr 28, 2016

@author: nconnors
'''
from vocollect_core.utilities import class_factory, obj_factory

from mlSharedConstants import PICK_BY_VOICE_TASK_NAME, WAREHOUSE_ORDER_SUMMARY, DIRECT_TO_AISLE, DIRECT_TO_STACK, \
    PICK_QUANTITY, INITIALIZE_PICK, VERIFY_PICK_LOCATION, VALIDATE_DEST_HU, INITIALIZE_DATA,\
    POST_DATA, PROCESS_ERROR_NOTIFICATION, VERIFY_DEST_HU, VALIDATE_PICK_LOCATION, VERIFY_BATCH,\
    POST_PICK, SET_LOCATION_STATE, SIGN_OFF_REASON, PRINT_LABEL, GOTO_MAIN_MENU
    
from tcodes.tcodeTaskBase import TcodeTaskBase
from voice import get_voice_application_property

from vocollect_core.dialog.functions import prompt_only, \
    prompt_ready, prompt_digits, prompt_yes_no, prompt_digits_required,\
    prompt_list
from vocollect_core.utilities.localization import itext
from jx_tcodes.PickByVoice_Vocabulary import PickByVoice_Vocabulary
from voice import log_message

#=============================================================================
# tcode PickByVoice used to process system pick by voice tcode
#=============================================================================
class PickByVoice(class_factory.get(TcodeTaskBase)):
    
    #----------------------------------------------------------
    def __init__(self, tcd, taskRunner=None, callingTask=None):
        
        super(PickByVoice, self).__init__(tcd, taskRunner, callingTask)

        # Set task name
        self.name = PICK_BY_VOICE_TASK_NAME
        
        self.vars = {}
                
        # create dynamic vocabulary for picking task
        self.dynamic_vocab = obj_factory.get(PickByVoice_Vocabulary, self.tcd, taskRunner)

        self.warehouseOrderNumber = itext('pbv.warehouse.order.number.not.defined')
        self.storageType = itext('pbv.storage.type.not.defined')
        self.packingMaterial = itext('pbv.packing.material.not.defined')
        self.umpPicking = itext('pbv.ump.picking.not.defined')
        
        # initialize pick location values
        self._current_aisle = ''
        self._current_stack = ''
        self._current_level = ''
        self._previous_aisle = ''
        self._previous_stack = ''
        self._previous_level = ''
        
        self._check_digits = ''
        self._requested_quantity = ''
        self._uom = ''
        
        self.firstPick = True
        self.zeroPick = False
                
        #  get number of trailing digits to use for spoken verification of dest HU
        self.spokenHULength = get_voice_application_property('SpokenHULength')

    #----------------------------------------------------------
    def initializeStates(self):
        '''set states '''
        self.addState(INITIALIZE_DATA, self.initializeData)
        self.addState(WAREHOUSE_ORDER_SUMMARY, self.warehouseOrderSummary)
        self.addState(INITIALIZE_PICK, self.initializePick)
        self.addState(SET_LOCATION_STATE, self.setLocationState)
        self.addState(DIRECT_TO_AISLE, self.directToAisle)
        self.addState(DIRECT_TO_STACK, self.directToStack)
        self.addState(VERIFY_PICK_LOCATION, self.verifyPickLocation)
        self.addState(VERIFY_BATCH, self.verifyBatch)
        self.addState(PICK_QUANTITY, self.pickQuantity)
        self.addState(VERIFY_DEST_HU, self.verifyDestHU)
        self.addState(PRINT_LABEL, self.printLabel)
        self.addState(POST_PICK, self.postPick)
        self.addState(POST_DATA, self.postData)
        self.addState(PROCESS_ERROR_NOTIFICATION, self.processErrorNotification)

    #----------------------------------------------------------
    def initializeData(self):
        ''' initializes data received from ITS and determines appropriate state
            to process the data  '''
        
        if self.tcd._current_screen == 'SAPLRF_PBV0200':
            self.next_state = WAREHOUSE_ORDER_SUMMARY
        elif self.tcd._current_screen in ['SAPLRF_PBV0501','SAPLRF_PBV0301']:
            self.next_state = INITIALIZE_PICK
        elif self.tcd._current_screen == 'SAPLRF_SSCR0013':
            self.next_state = PICK_QUANTITY
        elif self.tcd._current_screen == 'SAPLRF_SSCR0012':
            self.next_state = PROCESS_ERROR_NOTIFICATION
        elif self.tcd._current_screen == 'SAPLRF_SSCR0011':
            self.tcd._tcode ='MENU'
            self.next_state = ''
            
    #----------------------------------------------------------
    def warehouseOrderSummary(self):
        ''' warehouse order summary state '''
        
        # ---------------------------------------------
        # confirm that current screen is SAPLRF_PBV0200
        # ---------------------------------------------
        if self.tcd._current_screen != 'SAPLRF_PBV0200':
            # flow is bad - need to figure out how we got here and correct it!
            log_message('CRITICAL ERROR: entered WAREHOUSE_ORDER_SUMMARY state but current screen was not SAPLRF_PBV0200')
            log_message('current screen: ' + self.tcd._current_screen + ', previous screen: ' + self.tcd._previous_screen)
            prompt_ready(itext('error.unexpected.signing.off.message'))
            self.signOff()
            
        # ---------------------------------------------
        # populate local values from SAPLRF_PBV0200
        # ---------------------------------------------
        # initialize warehouse order number (abarradas:) and speak it to the operator
        self.warehouseOrderNumber = self.getValue('/SCWM/S_WHO_INT-WHO')
        if self.warehouseOrderNumber == '':
            self.warehouseOrderNumber = itext('pbv.warehouse.order.number.not.defined')
            result = prompt_ready(self.warehouseOrderNumber, additional_vocab = {'sign off':True})
        else:
            result = prompt_ready(itext('pbv.warehouse.order.number', self.warehouseOrderNumber), additional_vocab = {'sign off':True})
            
        if result == 'sign off':
            self.signOff()
        
        # initialize storage type
        self.storageType = self.getValue('/SCWM/S_WHO_INT-LGTYP')
        if self.storageType == '':
            self.storageType = itext('pbv.storage.type.not.defined')
        # initialize packing material
        self.packingMaterial = self.getValue('/scwm/s_rf_pick_hus-pmat[1]').lower()
        if self.packingMaterial == '':
            self.packingMaterial = itext('pbv.packing.material.not.defined.message')
        # abarradas: initialize ump picking
        self.umpPicking = self.getValue('/scwm/s_rf_pick_hus-huident[1]')
        if self.umpPicking == '':
            self.umpPicking = itext('pbv.ump.picking.not.defined')
        
        # ---------------------------------------------
        # Print label
        # abarradas
        # ---------------------------------------------
        okCode = self.getValue('/SCWM/S_RF_SCRELM-PB3')
        if okCode != None:
            # build name/value pairs
            self.buildNameValuePairs(okCode)
            self.post()
            # TODO abarradas: Check if current screen is error screen or other than SAPLRF_PBV0200
        else:
            # repeat state  - not sure how this could happen so not sure what to do about it
            self.next_state = self.current_state
        
        result = prompt_ready(itext('pbv.pick.summary.message',self.storageType,self.packingMaterial),additional_vocab = {'sign off':True})
        
        okCode = None
        if result == 'sign off':
            self.signOff()
        elif result == 'ready':
            okCode = self.getValue('/SCWM/S_RF_SCRELM-PB2')
            
        if okCode != None:
            # build name/value pairs
            self.buildNameValuePairs(okCode)
            
            self.next_state = POST_DATA
        else:
            # repeat state  - not sure how this could happen so not sure what to do about it
            self.next_state = self.current_state
            
        
    #----------------------------------------------------------
    def initializePick(self):
        ''' confirm pick data is available and initialize local values '''
        
        # ---------------------------------------------
        #  confirm that current screen is SAPLRF_PBV0501
        # ---------------------------------------------
        if self.tcd._current_screen not in ['SAPLRF_PBV0501','SAPLRF_PBV0301']:
            # flow is bad - need to figure out how we got here and correct it!
            log_message('CRITICAL ERROR: entered INITIALIZE_PICK state but current screen was not SAPLRF_PBVO501 or SAPLRF_PBV0301')
            log_message('current screen: ' + self.tcd._current_screen + ', previous screen: ' + self.tcd._previous_screen)
            prompt_ready(itext('error.unexpected.signing.off.message'))
            self.signOff()
        
        # ---------------------------------------------
        # populate local values from SAPLRF_PBV00501 or SAPLRF_PBV0301`
        # ---------------------------------------------
        # save previous location values
        self._previousAisle = self._current_aisle
        self._previousStack = self._current_stack
        self._previousLevel = self._current_level
        # populate new location  values from screen data
        self._current_aisle = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-AISLE')
        self._current_stack = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-STACK')
        self._current_level = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V')
        # initialize check digits for this pick location
        self._check_digits = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF.SpeechGrammar').strip()
        # initialize requested pick quantity
        self._requested_quantity = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-VSOLA_CHR')
        # initialize UoM with spoken mapped value
        self._uom = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-ALTME')
        
        # speak destination storage type when processing destination screen SAPLRF_PBV_301
        if self.tcd._current_screen == 'SAPLRF_PBV0301':
            # self.storage_type = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-NLTYP')
            # prompt_ready(itext('pbv.dest.storage.type.message',self.storage_type))
            
            # abarradas Destination screen to deposit. Next step is dispatch stage
            prompt_ready(itext('pbv.dest.deposit.message', self._current_aisle + self._current_stack + self._current_level))
            okCode = self.getValue('/SCWM/S_RF_SCRELM-PB2')
            if okCode != None:
                self.firstPick = True
                # set Level confirmation
                if self._check_digits == '':    
                    self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF',self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V'))
                else:
                    self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF',self._check_digits)
                # set destHU confirmation
                self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU_VERIF',self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU'))
                # build name/value pairs
                self.buildNameValuePairs(okCode)
                self.post()
            self.next_state = INITIALIZE_DATA

    #----------------------------------------------------------
    def setLocationState(self):
        ''' determines the first state to be executed when guiding worker to pick location '''
                
        # ---------------------------------------------
        # specify next state based on location parsing key
        # ---------------------------------------------
        if self.tcd.speakAislePrompt == True:
            return
        elif self.tcd.speakStackPrompt == True:
            self.next_state = DIRECT_TO_STACK
        else:
            self.next_state = VERIFY_PICK_LOCATION
            
    #----------------------------------------------------------
    def directToAisle(self):
        ''' guide the worker to the pick aisle '''
        
        # check to confirm that the previous aisle was different from the current aisle
        if self._current_aisle == self._previous_aisle or self._current_aisle == '':
            if self.tcd.speakStackPrompt == False:
                self.next_state = VERIFY_PICK_LOCATION
            # don't speak aisle prompt this time
            return
        
        result = prompt_ready(itext("pbv.aisle.prompt",self._current_aisle),additional_vocab = {'back':True,'next task':True,'sign off':True})

        if result == 'back':
            # build name/value pairs
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
            self.next_state = POST_DATA
        elif result == 'sign off':
            self.signOff()
        elif result == 'next task':
            self.nextWarehouseTask()

    #----------------------------------------------------------
    def directToStack(self):
        ''' guide the worker to the pick stack '''
        
        # check for blank stack
        if self._current_stack == '':
            return
        # check to confirm that the previous aisle and stack were different from the current ones
        if self._current_aisle == self._previous_aisle and \
                self._current_stack == self._previous_stack:
            # don't speak stack prompt this time
            return
        result = ''
        if self.tcd.speakAislePrompt == False:
            # if aisle is being combined with stack then speak both aisle and stack if aisle has changed
            if self._current_aisle != self._previous_aisle:
                result = prompt_ready(itext("pbv.aisle.stack.prompt",self._current_aisle,self._current_stack),additional_vocab = {'back':True,'next task':True})
        
        # only speak stack prompt and only if enabled
        elif self.tcd.speakStackPrompt == True:
            result = prompt_ready(itext("pbv.stack.prompt",self._current_stack),additional_vocab = {'back':True,'next task':True,'sign off':True})
        
        if result == 'back':
            # build name/value pairs
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
            self.next_state = POST_DATA
        elif result == 'sign off':
            self.signOff()
        elif result == 'next task':
            self.nextWarehouseTask()

    #----------------------------------------------------------
    def verifyPickLocation(self):
        ''' verify the pick location '''
        
        # determine type of prompt that is required
        # Reduced logical possibilities:
        # if stack prompt was spoken then level prompt is just level
        # If stack prompt was not spoken and aisle prompt was spoken then level prompt is stack and level
        # otherwise level prompt must speak all location components
        # abarradas, speak level and position
        if self.tcd.speakStackPrompt == True:
            prompt = itext('pbv.level.prompt', self._current_level[:2], self._current_level[2:])
        elif self.tcd.speakAislePrompt == True:
            prompt = itext('pbv.stack.level.prompt', self._current_stack,self._current_level)
        else:
            # must speak entire location
            prompt = itext('pbv.complete.location.prompt', self._current_aisle,self._current_stack,self._current_level)

        if self._check_digits == '':
            # check digit value will be an empty string if check digits are not specified and a level is not specified
            #  In this case, simply require that the operator say 'ready' to verify the pick location
            result = prompt_ready(prompt,additional_vocab = {'back':True,'next task':True,'sign off':True})
        else:
            # The standard verification is done using the value provided in the screen field /SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF.SpeechGrammar
            #  This value is set in SAP as the check digit value or the level if no check digits have been defined.
            result = prompt_digits(prompt, itext('pbv.check.digits.help'), min_length=1, max_length=3, confirm=True, additional_vocab = {'back':True,'next task':True,'sign off':True})
        
        if result == 'back':
            # build name/value pairs
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
            self.next_state = POST_DATA
            return
        elif result == 'sign off':
            self.signOff()
        elif result == 'next task':
            self.nextWarehouseTask()
            return            
        
        if self._check_digits == '':
            self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF',self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V'))
        else:
            locationDigits = self._check_digits
            if locationDigits == result:
                self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V_VERIF',self._check_digits)
            else:
                prompt_ready(itext('pbv.check.digits.error'))
                self.next_state = self.current_state
                return
            
        self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-AISLE_VERIF',self._current_aisle)
        self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-STACK_VERIF',self._current_stack)

    #----------------------------------------------------------
    def verifyBatch(self):
        ''' verifies batch if batch value is specified '''
        
        if self.tcd.confirmBatch == False:
            self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-BATCH_VERIF',self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH'))
            return
        
        batch = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH')
        
        if batch != '':
            result = prompt_ready(itext('pbv.verify.batch.prompt',batch),
                                  itext('pbv.verify.batch.prompt.help'),
                                  additional_vocab = {'back':True,'next task':True,'sign off':True})
            if result == 'back':
                # build name/value pairs
                self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
                self.next_state = POST_DATA
                return
            elif result == 'sign off':
                self.signOff()
            elif result == 'next task':
                self.nextWarehouseTask()
                return

        self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-BATCH_VERIF',batch)
        
    #----------------------------------------------------------
    def pickQuantity(self):
        ''' get the pick quantity '''
        self.zeroPick = False
        if self._requested_quantity == '':
            # this is the case for the destination screen
            # there is no quantity as part of the screen therefore
            # skip this state
            return
        # check for quantity > 1 which needs multiple UOM
        if self._requested_quantity > '1':
            uom = itext('UOM_' + self._uom + '_multiples')
            if uom == 'UOM__multiples':
                # indicates that there is no multiple UOM defined for this UOM
                uom = self._uom
        else:
            uom = itext('UOM_' + self._uom)
            if uom == 'UOM_' + self._uom:
                # indicates that there is no UOM translation defined for this UOM
                # only choice is to use value from SAP
                uom = self._uom
        
        result = prompt_digits(itext('pbv.quantity.prompt',self._requested_quantity,uom),
                               itext('pbv.quantity.prompt.help'),
                               confirm=False,additional_vocab = {'back':True,'next task':True,'sign off':True},
                               hints=self._requested_quantity)
            
        if result == 'back':
            # build name/value pairs
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
            self.next_state = POST_DATA
            return
        elif result == 'sign off':
            # abarradas Sign off not allowed
            prompt_only(itext('pcv.sign.off.not.allowed'))
            self.next_state = self.current_state
            return
        elif result == 'next task':
            self.nextWarehouseTask()
            return
        elif int(result) < int(self._requested_quantity):
            if prompt_yes_no(itext('pbv.confirm.short.pick', result, self._requested_quantity)):
                if self.tcd._current_screen != 'SAPLRF_SSCR0013':
                    # abarradas Push Exception button
                    self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-NISTA_VERIF',result)
                    okCode = self.getValue('/SCWM/S_RF_SCRELM-PB3')
                    if okCode != None:
                        # build name/value pairs
                        self.buildNameValuePairs(okCode)
                        self.post()
                    else:
                        # repeat state  - not sure how this could happen so not sure what to do about it
                        self.next_state = self.current_state
                        return
                
                # Current screen is SAPLRF_SSCR0013
                if self.tcd._current_screen == 'SAPLRF_SSCR0013':
                    if result == '0':
                        self.zeroPick = True
                        shortCode = self.getValue('/SCWM/S_RF_SCRELM-LISTVAL1')
                    else:
                        self.zeroPick = False
                        shortCode = self.getValue('/SCWM/S_RF_SCRELM-LISTVAL2')
                
                self.buildNameValuePairs(shortCode)
                self.post()
                if self.zeroPick:
                    self.next_state = INITIALIZE_DATA
                    return
            else:
                self.next_state = self.current_state
                return    
        elif int(result) > int(self._requested_quantity):
            prompt_only(itext('pbv.quantity.overpick.not.allowed'))
            self.next_state = self.current_state
            return
        
        self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-NISTA_VERIF',result)

    #----------------------------------------------------------
    def verifyDestHU(self):
        ''' verify the destination HU '''
        
        if self.tcd.confirmHU == False or not self.firstPick:
            self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU_VERIF',self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU'))
        else:
            if not self.zeroPick:
                destHU = self.getValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU')
                # get grammar values for use during validation
                spokenDestHU = destHU[-(int(self.spokenHULength)):]

                prompt = itext('pbv.verify.dest.hu.prompt')

                result = prompt_digits(prompt, itext('pbv.check.digits.help'), min_length=1, max_length=int(self.spokenHULength), confirm=True, additional_vocab = {'back':True,'next task':True,'sign off':True})
            
                if result == 'back':
                    # build name/value pairs
                    self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB1'))         
                    self.next_state = POST_DATA
                    return
                elif result == 'sign off':
                    self.signOff()
                elif result == 'next task':
                    self.nextWarehouseTask()
                    return

                if spokenDestHU == result:
                    self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU_VERIF',result)
                    self.firstPick = False
                else:
                    prompt_ready(itext('pbv.hu.error'))
                    self.next_state = self.current_state
                    return
            else:
                return

        
        # determine next state:
        # If screen is SAPLRF_PBV0501 then don't print label, go to post pick
        if self.tcd._current_screen == 'SAPLRF_PBV0501':
            self.next_state = POST_PICK

    #----------------------------------------------------------
    def printLabel(self):
        ''' automatically prints the HU label '''
        
        # build name/value pairs
        if not self.zeroPick:
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB8'))         
            self.post()
        else:
            return      
    
    #----------------------------------------------------------
    def postPick(self):
        ''' post pick data '''              
        # build name/value pairs
        if not self.zeroPick:
            self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB2'))
        else:
            return

    #----------------------------------------------------------
    def postData(self):
        ''' post data from this state - 
            because it will set next state to INITIALIZE_DATA where flow 
            to the next state will be directed based on the data returned 
            from the post '''
            
        self.next_state = INITIALIZE_DATA
        
        # post to SAP
        self.post()      

    #----------------------------------------------------------
    def processErrorNotification(self):
        ''' method to process message screen from SAP '''
        
        sign_off_request = False
        
        # build message to speak
        i = 1
        message = ''
        while i < 5:
            message += self.getValue('/SCWM/S_RF_SCRELM-MSGT' + str(i)) + ''
            i += 1

        # if error message is in HU error
        if itext('sap.msg.invalid.hu.number') == message:
            # destination HU number  - if message contains phrase 'E: Verificación de UMpDest no es válida(/SCWM/UI_RF020)'
            # then it will be treated as an error with the HU number
            #  Flow will be sent back to the destination HU state and
            # the storage bin verification value will be set again in case SAP clears
            # it out when it returns the screen.
            message = itext('pbv.hu.error')
            # clear out current HU value to trigger HU prompt for new value
            self.setValue('/SCWM/S_RF_ORDIM_CONFIRM-PICKHU_VERIF','')
            self.next_state = VERIFY_DEST_HU
        elif itext('sap.msg.invalid.check.digits') == message:
            # pick_location check digits  - if message contains phrase 'E: Verificación de Nivel no es válida(/SCWM/UI_RF020)'
            # then it will be treated as an error with the location number
            #  Flow will be sent back to the pick location state and
            # the storage bin verification value will be set again in case SAP clears
            # it out when it returns the screen.
            message = itext('pbv.check.digits.error')
            # clear out current HU value to trigger HU prompt for new value
            self._check_digits = ''
            self.next_state = VERIFY_PICK_LOCATION
        elif itext('sap.msg.exception.error') == message:
            # Confirmation exception code message - if message contains phrase 'E: Indique un código de excepción parael mensaje de diferencias(/SCWM/RF_EN003)'
            # then it will be not prompted
            okCode = self.getValue('/SCWM/S_RF_SCRELM-PB2')

            self.post()
            self.next_state = INITIALIZE_PICK
            return

        result = prompt_ready(message, additional_vocab = {'sign off':True})

        if result == 'sign off':
            sign_off_request = True

        self.post()
        
        # check for sign off request 
        if sign_off_request == True:
                self.signOff()

    #=======================================================================
    # END OF STATE FUNCTIONS - the remaining functions are utility methods
    #=======================================================================
    
    #----------------------------------------------------------
    def getStorageType(self):
        return self.storageType
        
    #----------------------------------------------------------
    def getWarehouseOrderNumber(self):
        return self.warehouseOrderNumber
        
    #----------------------------------------------------------
    def getUnitOfMeasure(self):
        
        uom = itext('UOM_' + self._uom)
        # check for valid mapping of UOM in properties file       
        if 'UOM_' in uom:
            # this indicates that there was no mapping 
            # check for blank uom value
            if self._uom == '':
                uom = itext('pbv.uom.not.available')
            else:
                # use raw value from SAP
                uom = self._uom
        
        return uom
        
    #----------------------------------------------------------
    def getQuantity(self):
        
        if self._requested_quantity == '':
            return itext('pbv.vocab.quantity.not.available')
        else:
        # check for quantity > 1 which needs multiple UOM
            if self._requested_quantity > '1':
                uom = itext('UOM_' + self._uom + '_multiples')
                if uom == 'UOM__multiples':
                    # indicates that there is no multiple UOM defined for this UOM
                    uom = self._uom
            else:
                uom = itext('UOM_' + self._uom)
                if uom == 'UOM_' +  self._uom:
                    uom = self._uom
        
        
        return self._requested_quantity + ' ' + uom
            
    #----------------------------------------------------------
    def nextWarehouseTask(self):
        ''' prepares to post the next task button to ITS and sets next state to POST_DATA  '''
        
        # build name/value pairs
        self.buildNameValuePairs(self.getValue('/SCWM/S_RF_SCRELM-PB11'))
        self.next_state = INITIALIZE_DATA
        
        # post to SAP
        self.post()      
        
    #----------------------------------------------------------
