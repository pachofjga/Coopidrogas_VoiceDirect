'''
Created on Apr 20, 2016

@author: nconnors
'''

#==============================================================================
# Task names
#==============================================================================
MLPROCESSOR_TASK_NAME = 'mlProcessor_task_name'
JUMEX_MLPROCESSOR_TASK_NAME = 'jumex_mlProcessor_task_name'
TCODE_TASK_BASE_NAME = 'tcode_task_base_name'
JUMEX_TCODE_TASK_BASE_NAME = 'jumex_tcode_task_base_name'
RLMENU_TASK_NAME = 'rlmenu_task_name'
JUMEX_RLMENU_TASK_NAME = 'jumex_rlmenu_task_name'
PICK_BY_VOICE_TASK_NAME = 'pick_by_voice_task_name'

#==============================================================================
# Tcodes
#==============================================================================
TCODE_PICK_BY_VOICE                 = 'PICKBYVOICE'

#==============================================================================
# PROCESS CONSTANTS
#==============================================================================
AUTO_RUN_STATE                      = 'autoRunState'
RETURN_TCODE                        = 'returnTcode'
AUTO_RUN_TCODE                      = 'autoRunTcode'

AUTO_RUN_NOT_ACTIVE                 = 0
AUTO_RUN_START                      = 1
AUTO_RUN_RETURN                     = 2

#==============================================================================
# Screen data dictionary entry constants
#==============================================================================
VALUE                               = 'value'
NAME                                = 'name'

#==============================================================================
# Vocabulary
#==============================================================================
VOCAB_BACK                          = 'back'
VOCAB_BATCH                         = 'batch'
VOCAB_LOCATION                      = 'location'
VOCAB_MAIN_MENU                     = 'main menu'
VOCAB_MATERIAL_NUMBER               = 'material number'
VOCAB_MATERIAL_DESCRIPTION          = 'material description'
VOCAB_NEXT_TASK                     = 'next task'
VOCAB_PACKING_MATERIAL              = 'packing material'
VOCAB_PLANT                         = 'plant'
VOCAB_PREVIOUS                      = 'previous'
VOCAB_PRINT                         = 'print'
VOCAB_PRINTER                       = 'printer'
VOCAB_QUANTITY                      = 'quantity'
VOCAB_UOM                           = 'unit of measure'
VOCAB_READY                         = 'ready'
VOCAB_STOP                          = 'stop'
VOCAB_STORAGE_TYPE                  = 'storage type'
VOCAB_SUMMARY                       = 'summary'
VOCAB_WO_NUMBER                     = 'warehouse order'
VOCAB_UMP_PICKING                   = 'ump picking'
VOCAB_LOT                           = 'lot'

#==============================================================================
# state definitions: RLMENU
#==============================================================================
GOTO_MAIN_MENU                      = 'gotoMainMenu'
SELECT_TCODE                        = 'selectTcode'
GOTO_TCODE_MENU                     = 'gotoTcodeMenu'
RUN_TCODE                           = 'runTcode'

#==============================================================================
# state definitions: PickByVoice
#==============================================================================
INITIALIZE_DATA                     = 'initializeData'
WAREHOUSE_ORDER_SUMMARY             = 'warehouseOrderSummary'  
INITIALIZE_PICK                     = 'initializePick' 
SET_LOCATION_STATE                  = 'setLocationState'       
DIRECT_TO_AISLE                     = 'directToAisle'
DIRECT_TO_STACK                     = 'directToStack'
VERIFY_PICK_LOCATION                = 'verifyPickLocation'
VALIDATE_PICK_LOCATION              = 'validateLocationConfirmation'
VERIFY_BATCH                        = 'verifyBatch'
PICK_QUANTITY                       = 'pickQuantity'
VERIFY_DEST_HU                      = 'verifyDestHU'
VALIDATE_DEST_HU                    = 'validateLocationConfirmation'
PRINT_LABEL                         = 'printLabel'
POST_PICK                           = 'postPick'
POST_DATA                           = 'postData'
PROCESS_ERROR_NOTIFICATION          = 'processErrorNotification'
SIGN_OFF_REASON                     = 'signOffReason'

#==============================================================================
# Button values for various screens
#==============================================================================
BACK_BUTTON_RLMENU =                        '/EBACK'
BACK_BUTTON_SAPLLMOB777 =                   'BACK'

#==============================================================================
# Error message constants
#==============================================================================
INVALID_OPERATOR_ID_FORMAT =                'invalid.operator.id.format'

