#-------------------------------------------------------------------------------
#  * Copyright (c) 2013 Vocollect, Inc.
#  * Pittsburgh, PA 15235
#  * All rights reserved.
#  *
#  * This source code contains confidential information that is owned by
#  * Vocollect, Inc. and may not be copied, disclosed or otherwise used without
#  * the express written consent of Vocollect, Inc.
#  
#-------------------------------------------------------------------------------
#from CreateTestFile import CreateTestFile
import mock_catalyst
import sys
mock_catalyst.environment_properties['WebServer.Port'] = '80'

from main import main
from mock_catalyst import EndOfApplication

#from vocollect_lut_odr_test.mock_server import MockServer, LUT_SERVER

''' To modify this file for test case generation see:  https://collab.vocollect.int/docs/DOC-8852 '''


# Uncomment and configure if you would like to use mock server 
#mock_server = MockServer(use_std_in_out = True)
#mock_server.start_server(LUT_SERVER)

''' To capture server request/responses for test case generation 
    set this mock_server property '''
#mock_server.set_pass_through_host('10.3.3.1', 15020)

mock_catalyst.environment_properties['Operator.Name'] = 'MEWDFMARIN'
#mock_catalyst.environment_properties['Operator.Id'] = 'OPER01-oper01'
mock_catalyst.environment_properties['Operator.Id'] = 'MEWDFMARIN'

mock_catalyst.environment_properties['Device.Id'] = '123456'
mock_catalyst.environment_properties['SwVersion.Locale'] = 'es_MX'


try:
    main()
except EndOfApplication as err:
    print('Application ended')
    
#mock_server.stop_server(LUT_SERVER)

# Un-comment below if you would like to see what was logged.
print('\n\nDumping mock_catalyst log messages buffer..................\\n')
for msg in mock_catalyst.log_messages:
    print(msg)

#Sample test case creation
#test = CreateTestFile('Sample', mock_server)
#path = '' #should end with slash if specified (i.e. test/vderp_test/system_tests/)
#test.write_test_to_file(path)
