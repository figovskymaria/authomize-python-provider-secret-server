"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.event_pipeline_policy_api import EventPipelinePolicyApi  # noqa: E501


class TestEventPipelinePolicyApi(unittest.TestCase):
    """EventPipelinePolicyApi unit test stubs"""

    def setUp(self):
        self.api = EventPipelinePolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_pipeline_policy_service_activate_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_activate_event_pipeline_policy

        Activate Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy

        Add Pipeline To Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_create_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_create_event_pipeline_policy

        Create Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_duplicate_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_duplicate_event_pipeline_policy

        Duplicate Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_export_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_export_event_pipeline_policy

        Export Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder(self):
        """Test case for event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder

        Get Child Folder Data For Pipeline Policy Folder  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_event_pipeline_policies(self):
        """Test case for event_pipeline_policy_service_get_event_pipeline_policies

        Get Event Pipeline Policies  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_get_event_pipeline_policy

        Get Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_event_pipeline_policy_run_activity(self):
        """Test case for event_pipeline_policy_service_get_event_pipeline_policy_run_activity

        Get Event Pipeline Policy Run Activity  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_event_pipeline_policy_runs(self):
        """Test case for event_pipeline_policy_service_get_event_pipeline_policy_runs

        Get Event Pipeline Policy Runs  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_folders_for_pipeline_policies(self):
        """Test case for event_pipeline_policy_service_get_folders_for_pipeline_policies

        Get Folders For Pipeline Policies  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_group_count_for_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_get_group_count_for_pipeline_policy

        Get Group Count For Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_groups_for_pipeline_policies(self):
        """Test case for event_pipeline_policy_service_get_groups_for_pipeline_policies

        Get Groups For Pipeline Policies  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_get_secret_policies_for_pipeline_policies(self):
        """Test case for event_pipeline_policy_service_get_secret_policies_for_pipeline_policies

        Get Secret Policies For Pipeline Policies  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_import_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_import_event_pipeline_policy

        Import Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_remove_event_pipeline_from_policy(self):
        """Test case for event_pipeline_policy_service_remove_event_pipeline_from_policy

        Remove Event Pipeline From Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_update_event_pipeline_policy(self):
        """Test case for event_pipeline_policy_service_update_event_pipeline_policy

        Update Event Pipeline Policy  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_update_event_pipeline_policy_folder_maps(self):
        """Test case for event_pipeline_policy_service_update_event_pipeline_policy_folder_maps

        Update Event Pipeline Policy Folder Maps  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_update_event_pipeline_policy_group_maps(self):
        """Test case for event_pipeline_policy_service_update_event_pipeline_policy_group_maps

        Update Event Pipeline Policy Group Maps  # noqa: E501
        """
        pass

    def test_event_pipeline_policy_service_update_event_pipeline_policy_sort_order(self):
        """Test case for event_pipeline_policy_service_update_event_pipeline_policy_sort_order

        Update Event Pipeline Policy Sort Order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()