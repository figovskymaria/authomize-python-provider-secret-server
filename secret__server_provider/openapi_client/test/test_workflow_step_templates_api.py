"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.workflow_step_templates_api import WorkflowStepTemplatesApi  # noqa: E501


class TestWorkflowStepTemplatesApi(unittest.TestCase):
    """WorkflowStepTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowStepTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workflow_step_templates_service_create_step(self):
        """Test case for workflow_step_templates_service_create_step

        Create Workflow Step  # noqa: E501
        """
        pass

    def test_workflow_step_templates_service_get_template_step(self):
        """Test case for workflow_step_templates_service_get_template_step

        Get a Workflow Template Step  # noqa: E501
        """
        pass

    def test_workflow_step_templates_service_get_template_steps(self):
        """Test case for workflow_step_templates_service_get_template_steps

        Get Workflow Template Steps  # noqa: E501
        """
        pass

    def test_workflow_step_templates_service_stub(self):
        """Test case for workflow_step_templates_service_stub

        Get a Workflow Template Step Stub  # noqa: E501
        """
        pass

    def test_workflow_step_templates_service_update_step(self):
        """Test case for workflow_step_templates_service_update_step

        Update Workflow Template Steps  # noqa: E501
        """
        pass

    def test_workflow_step_templates_service_update_step_model(self):
        """Test case for workflow_step_templates_service_update_step_model

        Update a Workflow Template Step  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
