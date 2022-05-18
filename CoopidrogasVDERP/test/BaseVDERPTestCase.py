#-------------------------------------------------------------------------------
#  Copyright 2016 Honeywell International Inc. All rights reserved. 
#-------------------------------------------------------------------------------
''' Extends the VoiceArtisan base test case and adds a couple methods
    specifically for validating VoiceLink formatted LUTs
'''
from vocollect_lut_odr_test.base_test_case_server import BaseTestCaseServer
from vocollect_lut_odr_test.mock_server import ODR_SERVER, LUT_SERVER, BOTH_SERVERS #@UnusedImport
from vocollect_core_test.base_test_case import EndOfApplication  #@UnusedImport
from vocollect_lut_odr.connections import OdrConnection
from vocollect_core.utilities import pickler
import os
import mock_catalyst
from vocollect_lut_odr_test.mock_server import MockServer

class BaseVDERPTestCase(BaseTestCaseServer):
    
    def __init__(self, methodName):
        super(BaseVDERPTestCase, self).__init__(methodName)

        #Change the ports from default 15008/15009 to 15004/15005
        #create simulated host server object
        self.mock_server = MockServer(True, 15020)
        
        # pass through functions to the mock server
        self.stop_server = self.mock_server.stop_server
        self.start_server = self.mock_server.start_server  
        self.set_server_response = self.mock_server.set_server_response
        self.load_server_responses = self.mock_server.load_server_responses


#        #made sure vehicle info is on for all tests
        if mock_catalyst.application_properties == None:
            mock_catalyst.load_configuration()
        mock_catalyst.application_properties['SaveState'] = 'false'
        pickler.save_state = False

    def clear(self):
        paths = []
        for connection in OdrConnection._connections:
            paths.append(OdrConnection._connections[connection].archive_path)

        try:
            OdrConnection.close_all_connections()
        except:
            pass
        
        for path in paths:            
            try:
                os.remove(path)
            except:
                pass

        super(BaseVDERPTestCase, self).clear()
    
    def validate_server_requests(self, *requests):
        '''Validates multiple server requests. 
        requests - requests is a variable number parameters each one a list that containers the request name, 
                   followed by expected parameters. Again excluding the date time stamp, operator, and serial 
                   number parameters'''
        for request in requests:
            self.validate_server_request(*request)    

        request = self.mock_server.get_server_request()
        self.assertEquals(request, None, 
                          'Another requests found: ' + str(self._parse_request(request)))
        
    """ =========================================================="""
    """ validate a lut request """
    """ =========================================================="""
    def validate_server_request(self, requestName, *args):
        '''Validates a single server request. 
        requestName - requestname is the expected command name. 
        args  - is a variable number of parameters that are expected in the LUT request 
                excluding the date time stamp, operator, and serial number parameters '''
        request = self.mock_server.get_server_request()
        self.assertNotEqual(request, None, 'request was None')

        request = request.replace('\n', '')
        request = request.replace('\r', '')
        
        #break up lut
        parts = request.split(",")
        commandName = parts.pop(0)
                

        #validate command name
        self.assertEqual(commandName, requestName)

        #validate number of parameters
        self.assertEquals(len(args)+3, len(parts))
        
        #TODO: Check for valid date/time
        date = parts.pop(0) #@UnusedVariable
        
        #validate serial number
        self.assertEqual('"Device.Id"', parts.pop(0))
        
        #validate operator
        self.assertEqual('"Operator.Id"', parts.pop(0))

        #validate remaining params
        for i in range(len(args)):
            if args[i] != '*':
                self.assertEqual("%s"  % args[i], parts[i], 
                                 "Parameter %s is %s, expected '%s'\nRequest was: %s" % (i, parts[i], args[i], request))

    
    def _parse_request(self, request):
        ''' turns request into list to make it easier to copy into tests '''
        
        if request is None:
            return None
        
        #strip carriage returns and line feeds
        request = request.replace('\n', '')
        request = request.replace('\r', '')
        
        #break up lut
        parts = request.split("(")
        commandName = parts[0]
        parts[1] = parts[1].replace(")", "")
        parts[1] = parts[1].replace("'", "")
        parts[1] = parts[1].replace('"', "")
        params = parts[1].split(",")
        params = params[3:]
        params.insert(0, commandName)
        return params 
        
        
