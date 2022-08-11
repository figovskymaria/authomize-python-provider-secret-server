"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import plugins
from plugins.model.configuration_ssh_command_menu_map_model import ConfigurationSshCommandMenuMapModel
from plugins.model.configuration_ssh_command_menu_model import ConfigurationSshCommandMenuModel
from plugins.model.ssh_command_blocklist_patch_model import SshCommandBlocklistPatchModel
from plugins.model.ssh_command_patch_model import SshCommandPatchModel
globals()['ConfigurationSshCommandMenuMapModel'] = ConfigurationSshCommandMenuMapModel
globals()['ConfigurationSshCommandMenuModel'] = ConfigurationSshCommandMenuModel
globals()['SshCommandBlocklistPatchModel'] = SshCommandBlocklistPatchModel
globals()['SshCommandPatchModel'] = SshCommandPatchModel
from plugins.model.configuration_ssh_command_import_model import ConfigurationSshCommandImportModel


class TestConfigurationSshCommandImportModel(unittest.TestCase):
    """ConfigurationSshCommandImportModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationSshCommandImportModel(self):
        """Test ConfigurationSshCommandImportModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigurationSshCommandImportModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
