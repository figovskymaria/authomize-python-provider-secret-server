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
    from plugins.model.edit_requires_options import EditRequiresOptions
    from plugins.model.list_type import ListType
    globals()['EditRequiresOptions'] = EditRequiresOptions
    globals()['ListType'] = ListType


class SecretTemplateFieldUpdateArgs(ModelNormal):
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
            'description': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'display_name': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'editable_permission': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'edit_requires': (EditRequiresOptions,),  # noqa: E501
            'field_slug_name': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'generate_password_character_set': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'generate_password_length': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'hide_on_view': (bool,),  # noqa: E501
            'history_length': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'is_expiration_field': (bool,),  # noqa: E501
            'is_file': (bool,),  # noqa: E501
            'is_indexable': (bool,),  # noqa: E501
            'is_notes': (bool,),  # noqa: E501
            'is_password': (bool,),  # noqa: E501
            'is_required': (bool,),  # noqa: E501
            'is_url': (bool,),  # noqa: E501
            'list_type': (ListType,),  # noqa: E501
            'must_encrypt': (bool,),  # noqa: E501
            'name': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'password_requirement_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'password_type_field_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'secret_template_field_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'sort_order': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'description': 'description',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'editable_permission': 'editablePermission',  # noqa: E501
        'edit_requires': 'editRequires',  # noqa: E501
        'field_slug_name': 'fieldSlugName',  # noqa: E501
        'generate_password_character_set': 'generatePasswordCharacterSet',  # noqa: E501
        'generate_password_length': 'generatePasswordLength',  # noqa: E501
        'hide_on_view': 'hideOnView',  # noqa: E501
        'history_length': 'historyLength',  # noqa: E501
        'is_expiration_field': 'isExpirationField',  # noqa: E501
        'is_file': 'isFile',  # noqa: E501
        'is_indexable': 'isIndexable',  # noqa: E501
        'is_notes': 'isNotes',  # noqa: E501
        'is_password': 'isPassword',  # noqa: E501
        'is_required': 'isRequired',  # noqa: E501
        'is_url': 'isUrl',  # noqa: E501
        'list_type': 'listType',  # noqa: E501
        'must_encrypt': 'mustEncrypt',  # noqa: E501
        'name': 'name',  # noqa: E501
        'password_requirement_id': 'passwordRequirementId',  # noqa: E501
        'password_type_field_id': 'passwordTypeFieldId',  # noqa: E501
        'secret_template_field_id': 'secretTemplateFieldId',  # noqa: E501
        'sort_order': 'sortOrder',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SecretTemplateFieldUpdateArgs - a model defined in OpenAPI

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
            description (bool, date, datetime, dict, float, int, list, str, none_type): Field description. [optional]  # noqa: E501
            display_name (bool, date, datetime, dict, float, int, list, str, none_type): Field display name. [optional]  # noqa: E501
            editable_permission (bool, date, datetime, dict, float, int, list, str, none_type): Who has editing rights. [optional]  # noqa: E501
            edit_requires (EditRequiresOptions): [optional]  # noqa: E501
            field_slug_name (bool, date, datetime, dict, float, int, list, str, none_type): Field Slug Name. [optional]  # noqa: E501
            generate_password_character_set (bool, date, datetime, dict, float, int, list, str, none_type): When this is set to true, the field data will be obfuscated during export. [optional]  # noqa: E501
            generate_password_length (bool, date, datetime, dict, float, int, list, str, none_type): Generate password length.  Only returned if user can manage secret templates. [optional]  # noqa: E501
            hide_on_view (bool): Hide this field when viewing. [optional]  # noqa: E501
            history_length (bool, date, datetime, dict, float, int, list, str, none_type): History length. [optional]  # noqa: E501
            is_expiration_field (bool): Is expiration field. [optional]  # noqa: E501
            is_file (bool): Is this field a file type. [optional]  # noqa: E501
            is_indexable (bool): Is able to be indexed. [optional]  # noqa: E501
            is_notes (bool): Is this field a notes field type. [optional]  # noqa: E501
            is_password (bool): Is this field a password field type. [optional]  # noqa: E501
            is_required (bool): Is this field required. [optional]  # noqa: E501
            is_url (bool): Is this field a url field type. [optional]  # noqa: E501
            list_type (ListType): [optional]  # noqa: E501
            must_encrypt (bool): Must encrypt.  Only returned if user can manage secret templates. [optional]  # noqa: E501
            name (bool, date, datetime, dict, float, int, list, str, none_type): Field name. [optional]  # noqa: E501
            password_requirement_id (bool, date, datetime, dict, float, int, list, str, none_type): ID For Password Requirement assigned to field. [optional]  # noqa: E501
            password_type_field_id (bool, date, datetime, dict, float, int, list, str, none_type): Type of password field. [optional]  # noqa: E501
            secret_template_field_id (bool, date, datetime, dict, float, int, list, str, none_type): Field Id. [optional]  # noqa: E501
            sort_order (bool, date, datetime, dict, float, int, list, str, none_type): Sort Order for Field. [optional]  # noqa: E501
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
        """SecretTemplateFieldUpdateArgs - a model defined in OpenAPI

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
            description (bool, date, datetime, dict, float, int, list, str, none_type): Field description. [optional]  # noqa: E501
            display_name (bool, date, datetime, dict, float, int, list, str, none_type): Field display name. [optional]  # noqa: E501
            editable_permission (bool, date, datetime, dict, float, int, list, str, none_type): Who has editing rights. [optional]  # noqa: E501
            edit_requires (EditRequiresOptions): [optional]  # noqa: E501
            field_slug_name (bool, date, datetime, dict, float, int, list, str, none_type): Field Slug Name. [optional]  # noqa: E501
            generate_password_character_set (bool, date, datetime, dict, float, int, list, str, none_type): When this is set to true, the field data will be obfuscated during export. [optional]  # noqa: E501
            generate_password_length (bool, date, datetime, dict, float, int, list, str, none_type): Generate password length.  Only returned if user can manage secret templates. [optional]  # noqa: E501
            hide_on_view (bool): Hide this field when viewing. [optional]  # noqa: E501
            history_length (bool, date, datetime, dict, float, int, list, str, none_type): History length. [optional]  # noqa: E501
            is_expiration_field (bool): Is expiration field. [optional]  # noqa: E501
            is_file (bool): Is this field a file type. [optional]  # noqa: E501
            is_indexable (bool): Is able to be indexed. [optional]  # noqa: E501
            is_notes (bool): Is this field a notes field type. [optional]  # noqa: E501
            is_password (bool): Is this field a password field type. [optional]  # noqa: E501
            is_required (bool): Is this field required. [optional]  # noqa: E501
            is_url (bool): Is this field a url field type. [optional]  # noqa: E501
            list_type (ListType): [optional]  # noqa: E501
            must_encrypt (bool): Must encrypt.  Only returned if user can manage secret templates. [optional]  # noqa: E501
            name (bool, date, datetime, dict, float, int, list, str, none_type): Field name. [optional]  # noqa: E501
            password_requirement_id (bool, date, datetime, dict, float, int, list, str, none_type): ID For Password Requirement assigned to field. [optional]  # noqa: E501
            password_type_field_id (bool, date, datetime, dict, float, int, list, str, none_type): Type of password field. [optional]  # noqa: E501
            secret_template_field_id (bool, date, datetime, dict, float, int, list, str, none_type): Field Id. [optional]  # noqa: E501
            sort_order (bool, date, datetime, dict, float, int, list, str, none_type): Sort Order for Field. [optional]  # noqa: E501
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
