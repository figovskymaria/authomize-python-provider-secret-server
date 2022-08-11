"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plugins.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plugins.exceptions import ApiAttributeError


def lazy_import():
    from plugins.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
    from plugins.model.update_field_value_of_force_require_ticket_system_options import UpdateFieldValueOfForceRequireTicketSystemOptions
    from plugins.model.update_field_value_of_optional_bmc_change_management_comment_work_type import UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType
    from plugins.model.update_field_value_of_optional_bmc_incident_management_comment_work_type import UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType
    from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
    from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
    from plugins.model.update_field_value_of_ticket_system_types import UpdateFieldValueOfTicketSystemTypes
    globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
    globals()['UpdateFieldValueOfForceRequireTicketSystemOptions'] = UpdateFieldValueOfForceRequireTicketSystemOptions
    globals()['UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType'] = UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType
    globals()['UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType'] = UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType
    globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
    globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
    globals()['UpdateFieldValueOfTicketSystemTypes'] = UpdateFieldValueOfTicketSystemTypes


class TicketSystemPatchModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'active': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'add_comments_to_ticket': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'bmc_change_management_comment_work_type': (UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType,),  # noqa: E501
            'bmc_incident_management_comment_work_type': (UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType,),  # noqa: E501
            'bmc_remedy_authentication': (UpdateFieldValueOfString,),  # noqa: E501
            'bmc_remedy_url_endpoint': (UpdateFieldValueOfString,),  # noqa: E501
            'description': (UpdateFieldValueOfString,),  # noqa: E501
            'display_message': (UpdateFieldValueOfString,),  # noqa: E501
            'force_require_ticket_number': (UpdateFieldValueOfForceRequireTicketSystemOptions,),  # noqa: E501
            'is_default': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'name': (UpdateFieldValueOfString,),  # noqa: E501
            'power_shell_add_comment_script_arguments': (UpdateFieldValueOfString,),  # noqa: E501
            'power_shell_add_comment_script_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'power_shell_add_ticket_comment_script_arguments': (UpdateFieldValueOfString,),  # noqa: E501
            'power_shell_add_ticket_comment_script_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'power_shell_run_as_account_secret_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'power_shell_ticket_status_script_arguments': (UpdateFieldValueOfString,),  # noqa: E501
            'power_shell_ticket_status_script_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'service_now_allowed_statuses': (UpdateFieldValueOfString,),  # noqa: E501
            'service_now_domain_name': (UpdateFieldValueOfString,),  # noqa: E501
            'site_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'system_credential_secret_id': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'ticket_number_error_message': (UpdateFieldValueOfString,),  # noqa: E501
            'ticket_number_validation': (UpdateFieldValueOfString,),  # noqa: E501
            'ticket_system_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ticket_system_type': (UpdateFieldValueOfTicketSystemTypes,),  # noqa: E501
            'view_ticket_url': (UpdateFieldValueOfString,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active': 'active',  # noqa: E501
        'add_comments_to_ticket': 'addCommentsToTicket',  # noqa: E501
        'bmc_change_management_comment_work_type': 'bmcChangeManagementCommentWorkType',  # noqa: E501
        'bmc_incident_management_comment_work_type': 'bmcIncidentManagementCommentWorkType',  # noqa: E501
        'bmc_remedy_authentication': 'bmcRemedyAuthentication',  # noqa: E501
        'bmc_remedy_url_endpoint': 'bmcRemedyUrlEndpoint',  # noqa: E501
        'description': 'description',  # noqa: E501
        'display_message': 'displayMessage',  # noqa: E501
        'force_require_ticket_number': 'forceRequireTicketNumber',  # noqa: E501
        'is_default': 'isDefault',  # noqa: E501
        'name': 'name',  # noqa: E501
        'power_shell_add_comment_script_arguments': 'powerShellAddCommentScriptArguments',  # noqa: E501
        'power_shell_add_comment_script_id': 'powerShellAddCommentScriptId',  # noqa: E501
        'power_shell_add_ticket_comment_script_arguments': 'powerShellAddTicketCommentScriptArguments',  # noqa: E501
        'power_shell_add_ticket_comment_script_id': 'powerShellAddTicketCommentScriptId',  # noqa: E501
        'power_shell_run_as_account_secret_id': 'powerShellRunAsAccountSecretId',  # noqa: E501
        'power_shell_ticket_status_script_arguments': 'powerShellTicketStatusScriptArguments',  # noqa: E501
        'power_shell_ticket_status_script_id': 'powerShellTicketStatusScriptId',  # noqa: E501
        'service_now_allowed_statuses': 'serviceNowAllowedStatuses',  # noqa: E501
        'service_now_domain_name': 'serviceNowDomainName',  # noqa: E501
        'site_id': 'siteId',  # noqa: E501
        'system_credential_secret_id': 'systemCredentialSecretId',  # noqa: E501
        'ticket_number_error_message': 'ticketNumberErrorMessage',  # noqa: E501
        'ticket_number_validation': 'ticketNumberValidation',  # noqa: E501
        'ticket_system_id': 'ticketSystemId',  # noqa: E501
        'ticket_system_type': 'ticketSystemType',  # noqa: E501
        'view_ticket_url': 'viewTicketUrl',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TicketSystemPatchModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            add_comments_to_ticket (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            bmc_change_management_comment_work_type (UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType): [optional]  # noqa: E501
            bmc_incident_management_comment_work_type (UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType): [optional]  # noqa: E501
            bmc_remedy_authentication (UpdateFieldValueOfString): [optional]  # noqa: E501
            bmc_remedy_url_endpoint (UpdateFieldValueOfString): [optional]  # noqa: E501
            description (UpdateFieldValueOfString): [optional]  # noqa: E501
            display_message (UpdateFieldValueOfString): [optional]  # noqa: E501
            force_require_ticket_number (UpdateFieldValueOfForceRequireTicketSystemOptions): [optional]  # noqa: E501
            is_default (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            name (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_comment_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_comment_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_add_ticket_comment_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_ticket_comment_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_run_as_account_secret_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_ticket_status_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_ticket_status_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            service_now_allowed_statuses (UpdateFieldValueOfString): [optional]  # noqa: E501
            service_now_domain_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            site_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            system_credential_secret_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            ticket_number_error_message (UpdateFieldValueOfString): [optional]  # noqa: E501
            ticket_number_validation (UpdateFieldValueOfString): [optional]  # noqa: E501
            ticket_system_id (bool, date, datetime, dict, float, int, list, str, none_type): TicketSystemId. [optional]  # noqa: E501
            ticket_system_type (UpdateFieldValueOfTicketSystemTypes): [optional]  # noqa: E501
            view_ticket_url (UpdateFieldValueOfString): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TicketSystemPatchModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            add_comments_to_ticket (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            bmc_change_management_comment_work_type (UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType): [optional]  # noqa: E501
            bmc_incident_management_comment_work_type (UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType): [optional]  # noqa: E501
            bmc_remedy_authentication (UpdateFieldValueOfString): [optional]  # noqa: E501
            bmc_remedy_url_endpoint (UpdateFieldValueOfString): [optional]  # noqa: E501
            description (UpdateFieldValueOfString): [optional]  # noqa: E501
            display_message (UpdateFieldValueOfString): [optional]  # noqa: E501
            force_require_ticket_number (UpdateFieldValueOfForceRequireTicketSystemOptions): [optional]  # noqa: E501
            is_default (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            name (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_comment_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_comment_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_add_ticket_comment_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_add_ticket_comment_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_run_as_account_secret_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            power_shell_ticket_status_script_arguments (UpdateFieldValueOfString): [optional]  # noqa: E501
            power_shell_ticket_status_script_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            service_now_allowed_statuses (UpdateFieldValueOfString): [optional]  # noqa: E501
            service_now_domain_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            site_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            system_credential_secret_id (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            ticket_number_error_message (UpdateFieldValueOfString): [optional]  # noqa: E501
            ticket_number_validation (UpdateFieldValueOfString): [optional]  # noqa: E501
            ticket_system_id (bool, date, datetime, dict, float, int, list, str, none_type): TicketSystemId. [optional]  # noqa: E501
            ticket_system_type (UpdateFieldValueOfTicketSystemTypes): [optional]  # noqa: E501
            view_ticket_url (UpdateFieldValueOfString): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
