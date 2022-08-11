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
from plugins.model.update_field_value_of_secret_policy_data_item_of_optional_boolean import UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean
from plugins.model.update_field_value_of_secret_policy_data_item_of_optional_command_restriction_type import UpdateFieldValueOfSecretPolicyDataItemOfOptionalCommandRestrictionType
from plugins.model.update_field_value_of_secret_policy_data_item_of_optional_guid import UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid
from plugins.model.update_field_value_of_secret_policy_data_item_of_optional_int32 import UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32
from plugins.model.update_field_value_of_secret_policy_data_item_of_ssh_command_menu_group_model_array import UpdateFieldValueOfSecretPolicyDataItemOfSshCommandMenuGroupModelArray
from plugins.model.update_field_value_of_secret_policy_data_item_of_user_group_map_data_model_array import UpdateFieldValueOfSecretPolicyDataItemOfUserGroupMapDataModelArray
globals()['UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean'] = UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean
globals()['UpdateFieldValueOfSecretPolicyDataItemOfOptionalCommandRestrictionType'] = UpdateFieldValueOfSecretPolicyDataItemOfOptionalCommandRestrictionType
globals()['UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid'] = UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid
globals()['UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32'] = UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32
globals()['UpdateFieldValueOfSecretPolicyDataItemOfSshCommandMenuGroupModelArray'] = UpdateFieldValueOfSecretPolicyDataItemOfSshCommandMenuGroupModelArray
globals()['UpdateFieldValueOfSecretPolicyDataItemOfUserGroupMapDataModelArray'] = UpdateFieldValueOfSecretPolicyDataItemOfUserGroupMapDataModelArray
from plugins.model.secret_policy_security_items_update_model import SecretPolicySecurityItemsUpdateModel


class TestSecretPolicySecurityItemsUpdateModel(unittest.TestCase):
    """SecretPolicySecurityItemsUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicySecurityItemsUpdateModel(self):
        """Test SecretPolicySecurityItemsUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicySecurityItemsUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
