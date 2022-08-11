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
from plugins.model.configuration_advanced_update_args import ConfigurationAdvancedUpdateArgs
from plugins.model.configuration_application_settings_patch_model import ConfigurationApplicationSettingsPatchModel
from plugins.model.configuration_email_patch_model import ConfigurationEmailPatchModel
from plugins.model.configuration_folders_patch_model import ConfigurationFoldersPatchModel
from plugins.model.configuration_launcher_settings_patch_model import ConfigurationLauncherSettingsPatchModel
from plugins.model.configuration_local_password_patch_model import ConfigurationLocalPasswordPatchModel
from plugins.model.configuration_login_patch_model import ConfigurationLoginPatchModel
from plugins.model.configuration_permission_options_patch_model import ConfigurationPermissionOptionsPatchModel
from plugins.model.configuration_protocol_handler_settings_patch_model import ConfigurationProtocolHandlerSettingsPatchModel
from plugins.model.configuration_saml_patch_model import ConfigurationSamlPatchModel
from plugins.model.configuration_security_patch_model import ConfigurationSecurityPatchModel
from plugins.model.configuration_session_recording_patch_model import ConfigurationSessionRecordingPatchModel
from plugins.model.configuration_ssh_command_import_model import ConfigurationSshCommandImportModel
from plugins.model.configuration_ticket_system_list_create_or_patch_model import ConfigurationTicketSystemListCreateOrPatchModel
from plugins.model.configuration_user_experience_patch_model import ConfigurationUserExperiencePatchModel
from plugins.model.configuration_user_interface_patch_model import ConfigurationUserInterfacePatchModel
from plugins.model.license_model import LicenseModel
globals()['ConfigurationAdvancedUpdateArgs'] = ConfigurationAdvancedUpdateArgs
globals()['ConfigurationApplicationSettingsPatchModel'] = ConfigurationApplicationSettingsPatchModel
globals()['ConfigurationEmailPatchModel'] = ConfigurationEmailPatchModel
globals()['ConfigurationFoldersPatchModel'] = ConfigurationFoldersPatchModel
globals()['ConfigurationLauncherSettingsPatchModel'] = ConfigurationLauncherSettingsPatchModel
globals()['ConfigurationLocalPasswordPatchModel'] = ConfigurationLocalPasswordPatchModel
globals()['ConfigurationLoginPatchModel'] = ConfigurationLoginPatchModel
globals()['ConfigurationPermissionOptionsPatchModel'] = ConfigurationPermissionOptionsPatchModel
globals()['ConfigurationProtocolHandlerSettingsPatchModel'] = ConfigurationProtocolHandlerSettingsPatchModel
globals()['ConfigurationSamlPatchModel'] = ConfigurationSamlPatchModel
globals()['ConfigurationSecurityPatchModel'] = ConfigurationSecurityPatchModel
globals()['ConfigurationSessionRecordingPatchModel'] = ConfigurationSessionRecordingPatchModel
globals()['ConfigurationSshCommandImportModel'] = ConfigurationSshCommandImportModel
globals()['ConfigurationTicketSystemListCreateOrPatchModel'] = ConfigurationTicketSystemListCreateOrPatchModel
globals()['ConfigurationUserExperiencePatchModel'] = ConfigurationUserExperiencePatchModel
globals()['ConfigurationUserInterfacePatchModel'] = ConfigurationUserInterfacePatchModel
globals()['LicenseModel'] = LicenseModel
from plugins.model.secret_server_settings_patch_model import SecretServerSettingsPatchModel


class TestSecretServerSettingsPatchModel(unittest.TestCase):
    """SecretServerSettingsPatchModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretServerSettingsPatchModel(self):
        """Test SecretServerSettingsPatchModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretServerSettingsPatchModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()