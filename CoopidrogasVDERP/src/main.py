#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
# This is the driver module for the voice application.


from runner.app_runner import app_runner_startup
from vocollect_http.httpserver import server_startup
from web.handler import ExampleHandler
from vocollect_core import scanning
from voice import get_voice_application_property
import voice

# overrides
import jx_tcodes.jumex_rlmenu  #@UnusedImport
import jx_tcodes.jumex_tcodeData   #@UnusedImport
import jx_tcodes.jumex_tcodeTaskBase   #@UnusedImport
import jx_processor.jumex_mlProcessor   #@UnusedImport

# This is the driver function for the voice application.
def main():

    # Enabling triggered scanning
    use_trigger_scan_vocab = get_voice_application_property('UseTriggerScanVocab')
     
    voice.log_message("Use Trigger scan vocab value is : "+use_trigger_scan_vocab)
    if use_trigger_scan_vocab == 'true':
        trigger_scan_timeout = int(get_voice_application_property('TriggerScanTimeout'))
        scanning.set_trigger_vocab('scan')
        scanning.set_trigger_timeout(trigger_scan_timeout)
        
    
    ''' This will start the http server if it is enabled through useHTTPServer
         in voiceconfig.xml.'''
    server_startup(ExampleHandler)
    
    # Add additional application start-up logic here
    app_runner_startup()