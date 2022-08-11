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
from plugins.model.character_set_summary import CharacterSetSummary
from plugins.model.password_requirement_type import PasswordRequirementType
globals()['CharacterSetSummary'] = CharacterSetSummary
globals()['PasswordRequirementType'] = PasswordRequirementType
from plugins.model.password_requirement_rule_summary import PasswordRequirementRuleSummary


class TestPasswordRequirementRuleSummary(unittest.TestCase):
    """PasswordRequirementRuleSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPasswordRequirementRuleSummary(self):
        """Test PasswordRequirementRuleSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PasswordRequirementRuleSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()