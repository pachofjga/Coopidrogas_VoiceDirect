'''
Created on May 29, 2016

@author: nconnors
'''
from vocollect_core.utilities import class_factory, obj_factory
from vocollect_core.task.dynamic_vocabulary import DynamicVocabulary, Vocabulary
from mlSharedConstants import VOCAB_BATCH, VOCAB_LOCATION, \
        VOCAB_MATERIAL_NUMBER, VOCAB_QUANTITY, PICK_BY_VOICE_TASK_NAME, VOCAB_WO_NUMBER, \
        VOCAB_MATERIAL_DESCRIPTION, WAREHOUSE_ORDER_SUMMARY, VOCAB_STORAGE_TYPE,\
    VOCAB_UOM, DIRECT_TO_AISLE, DIRECT_TO_STACK, INITIALIZE_PICK, VERIFY_BATCH,\
    VERIFY_DEST_HU, VERIFY_PICK_LOCATION, TCODE_PICK_BY_VOICE,\
    VOCAB_PACKING_MATERIAL, PICK_QUANTITY, VOCAB_NEXT_TASK, VOCAB_UMP_PICKING,\
    VOCAB_LOT
from vocollect_core.task.task_runner import TaskRunnerBase
from vocollect_core.utilities.localization import itext
from vocollect_core.dialog.functions import prompt_only

#==============================================================================
class PickByVoice_Vocabulary(class_factory.get(DynamicVocabulary)):
    ''' Definition of additional vocabulary used throughout system guided picking
    
    Parameters
            runner - Task runner object
    '''
    
    def __init__(self, tcd, runner):
        self.vocabs = { VOCAB_BATCH:                    obj_factory.get(Vocabulary,VOCAB_BATCH,                 self._batch, False),
                        VOCAB_LOCATION:                 obj_factory.get(Vocabulary,VOCAB_LOCATION,              self._location, False),
                        VOCAB_MATERIAL_NUMBER:          obj_factory.get(Vocabulary,VOCAB_MATERIAL_NUMBER,       self._material_number, False),
                        VOCAB_MATERIAL_DESCRIPTION:     obj_factory.get(Vocabulary,VOCAB_MATERIAL_DESCRIPTION,  self._material_description, False),
                        VOCAB_QUANTITY:                 obj_factory.get(Vocabulary,VOCAB_QUANTITY,              self._quantity, False),
                        VOCAB_STORAGE_TYPE:             obj_factory.get(Vocabulary,VOCAB_STORAGE_TYPE,          self._storage_type, False),
                        VOCAB_PACKING_MATERIAL:         obj_factory.get(Vocabulary,VOCAB_PACKING_MATERIAL,      self._packing_material, False),
                        VOCAB_UOM:                      obj_factory.get(Vocabulary,VOCAB_UOM,                   self._unit_of_measure, False),
                        VOCAB_WO_NUMBER:                obj_factory.get(Vocabulary,VOCAB_WO_NUMBER,             self._wo_number, False),
                        VOCAB_UMP_PICKING:              obj_factory.get(Vocabulary,VOCAB_UMP_PICKING,           self._ump_picking, False),
                        VOCAB_LOT:                      obj_factory.get(Vocabulary,VOCAB_LOT,                   self._lot, False)}
                        
        self.tcd = tcd
        self.runner = runner

    #--------------------------------------------------------------------------
    def _valid(self, vocab):
        ''' Determines if a vocabulary word is currently valid
        
        Parameters:
                vocab - vocabulary word to check
                
        returns - True if word is valid at this time, otherwise false
        '''
        
        ''' available states in PBV task:
                add PBV task states here for easy reference when adding vocab
                '''
        
        task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
                
        if vocab == VOCAB_BATCH:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False       
                
        elif vocab == VOCAB_LOCATION:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_MATERIAL_NUMBER:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_MATERIAL_DESCRIPTION:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
        
        elif vocab == VOCAB_LOT:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_PACKING_MATERIAL:
            if task != None:
                if task.current_state not in [WAREHOUSE_ORDER_SUMMARY,INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_QUANTITY:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_STORAGE_TYPE:
            if task != None:
                if task.current_state not in [WAREHOUSE_ORDER_SUMMARY,INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_UOM:
            if task != None:
                if task.current_state not in [INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        elif vocab == VOCAB_WO_NUMBER:
            if task != None:
                if task.current_state not in [WAREHOUSE_ORDER_SUMMARY,INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
        
        elif vocab == VOCAB_UMP_PICKING:
            if task != None:
                if task.current_state not in [WAREHOUSE_ORDER_SUMMARY,INITIALIZE_PICK,DIRECT_TO_AISLE,DIRECT_TO_STACK,VERIFY_PICK_LOCATION,VERIFY_BATCH,PICK_QUANTITY,VERIFY_DEST_HU]:
                    return False
                else:
                    return True
            return False
                
        return False
    
    #--------------------------------------------------------------------------
    def _batch(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            # speak batch or no batch available
            if self.tcd.v == None or task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH') == '':
                prompt_only(itext('pbv.batch.not.available')) 
            else:
                prompt_only(itext('pbv.batch.vocab',task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH')))        
        return True 

    #--------------------------------------------------------------------------
    def _location(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:  
            if self.tcd.v != None:
                prompt = ''
                aisle = task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-AISLE')
                stack = task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-STACK')
                level = task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-LVL_V')
                if aisle != '':
                    prompt = itext('pbv.vocab.aisle.prompt',aisle) + ', '
                prompt += itext('pbv.vocab.stack.level.prompt',stack,level) 
                prompt_only(prompt)
                return True
        
        prompt_only(itext('pbv.vocab.location.not.available')) 
 
        return True 

    #--------------------------------------------------------------------------
    def _material_number(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            if self.tcd.v == None or task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-MATNR') == '':
                prompt_only(itext('pbv.material.not.available')) 
            else:
                prompt_only(itext('pbv.vocab.material.number',task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-MATNR')))
                
        return True 

    #--------------------------------------------------------------------------
    def _material_description(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            if self.tcd.v == None or task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-MAKTX') == '':
                prompt_only(itext('pbv.material.description.not.available')) 
            else:
                prompt_only(itext('pbv.vocab.material.description',task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-MAKTX').lower()))
        return True
    
    #--------------------------------------------------------------------------
    def _lot(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:
            if self.tcd.v == None or task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH') == '':
                prompt_only(itext('pbv.lot.not.available')) 
            else:
                prompt_only(itext('pbv.vocab.lot',task.getValue('/SCWM/S_RF_ORDIM_CONFIRM-RFBATCH')))
        return True

    #--------------------------------------------------------------------------
    def _packing_material(self):
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            if self.tcd.v == None or task.packingMaterial == '':
                prompt_only(itext('pbv.packing.material.not.defined')) 
            else:
                prompt_only(itext('pbv.vocab.packing.material',task.packingMaterial))
        return True 

    #--------------------------------------------------------------------------
    def _quantity(self):

        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            prompt_only(task.getQuantity())

        return True 

    #--------------------------------------------------------------------------
    def _storage_type(self):

        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            prompt_only(task.storageType)
        return True 

    #--------------------------------------------------------------------------
    def _unit_of_measure(self):

        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            prompt_only(task.getUnitOfMeasure())
        return True 


    #--------------------------------------------------------------------------
    def _wo_number(self):
        ''' warehouse order number '''
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            prompt_only(task.warehouseOrderNumber)
        return True 

    #--------------------------------------------------------------------------
    def _ump_picking(self):
        ''' warehouse order number '''
        
        task = None
        if self.tcd._tcode == TCODE_PICK_BY_VOICE: 
            task = TaskRunnerBase.get_main_runner().findTask(PICK_BY_VOICE_TASK_NAME)
            
        if task != None:            
            prompt_only(task.umpPicking)
        return True 

    #--------------------------------------------------------------------------

