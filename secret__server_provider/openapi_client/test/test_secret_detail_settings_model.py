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
from plugins.model.jumpbox_route_summary_model import JumpboxRouteSummaryModel
from plugins.model.one_time_password_settings_model import OneTimePasswordSettingsModel
from plugins.model.rdp_launcher_settings_model import RdpLauncherSettingsModel
from plugins.model.secret_detail_expiration_type import SecretDetailExpirationType
from plugins.model.ssh_launcher_settings_model import SshLauncherSettingsModel
globals()['JumpboxRouteSummaryModel'] = JumpboxRouteSummaryModel
globals()['OneTimePasswordSettingsModel'] = OneTimePasswordSettingsModel
globals()['RdpLauncherSettingsModel'] = RdpLauncherSettingsModel
globals()['SecretDetailExpirationType'] = SecretDetailExpirationType
globals()['SshLauncherSettingsModel'] = SshLauncherSettingsModel
from plugins.model.secret_detail_settings_model import SecretDetailSettingsModel


class TestSecretDetailSettingsModel(unittest.TestCase):
    """SecretDetailSettingsModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretDetailSettingsModel(self):
        """Test SecretDetailSettingsModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretDetailSettingsModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()