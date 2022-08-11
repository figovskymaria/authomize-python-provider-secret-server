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
from plugins.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
from plugins.model.domain_name_index_expire_update_model import DomainNameIndexExpireUpdateModel


class TestDomainNameIndexExpireUpdateModel(unittest.TestCase):
    """DomainNameIndexExpireUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDomainNameIndexExpireUpdateModel(self):
        """Test DomainNameIndexExpireUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DomainNameIndexExpireUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
