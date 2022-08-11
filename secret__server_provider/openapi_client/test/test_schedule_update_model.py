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
from plugins.model.update_field_value_of_date_time import UpdateFieldValueOfDateTime
from plugins.model.update_field_value_of_int32_array import UpdateFieldValueOfInt32Array
from plugins.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from plugins.model.update_field_value_of_optional_schedule_monthly_day_order_type import UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType
from plugins.model.update_field_value_of_optional_schedule_monthly_day_type import UpdateFieldValueOfOptionalScheduleMonthlyDayType
from plugins.model.update_field_value_of_optional_schedule_monthly_type import UpdateFieldValueOfOptionalScheduleMonthlyType
from plugins.model.update_field_value_of_schedule_change_type import UpdateFieldValueOfScheduleChangeType
from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfDateTime'] = UpdateFieldValueOfDateTime
globals()['UpdateFieldValueOfInt32Array'] = UpdateFieldValueOfInt32Array
globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType'] = UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType
globals()['UpdateFieldValueOfOptionalScheduleMonthlyDayType'] = UpdateFieldValueOfOptionalScheduleMonthlyDayType
globals()['UpdateFieldValueOfOptionalScheduleMonthlyType'] = UpdateFieldValueOfOptionalScheduleMonthlyType
globals()['UpdateFieldValueOfScheduleChangeType'] = UpdateFieldValueOfScheduleChangeType
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from plugins.model.schedule_update_model import ScheduleUpdateModel


class TestScheduleUpdateModel(unittest.TestCase):
    """ScheduleUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduleUpdateModel(self):
        """Test ScheduleUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScheduleUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
