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
from plugins.model.schedule_update_model import ScheduleUpdateModel
from plugins.model.update_field_value_of_optional_date_time import UpdateFieldValueOfOptionalDateTime
from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from plugins.model.update_field_value_of_optional_report_schedule_date_parameter_type import UpdateFieldValueOfOptionalReportScheduleDateParameterType
from plugins.model.update_field_value_of_report_format import UpdateFieldValueOfReportFormat
from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['ScheduleUpdateModel'] = ScheduleUpdateModel
globals()['UpdateFieldValueOfOptionalDateTime'] = UpdateFieldValueOfOptionalDateTime
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfOptionalReportScheduleDateParameterType'] = UpdateFieldValueOfOptionalReportScheduleDateParameterType
globals()['UpdateFieldValueOfReportFormat'] = UpdateFieldValueOfReportFormat
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from plugins.model.report_schedule_update_model import ReportScheduleUpdateModel


class TestReportScheduleUpdateModel(unittest.TestCase):
    """ReportScheduleUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportScheduleUpdateModel(self):
        """Test ReportScheduleUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportScheduleUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()