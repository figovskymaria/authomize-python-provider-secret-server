"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plugins.api_client import ApiClient, Endpoint as _Endpoint
from plugins.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.entity_type_model import EntityTypeModel
from plugins.model.event_subscription_create_args import EventSubscriptionCreateArgs
from plugins.model.event_subscription_model import EventSubscriptionModel
from plugins.model.event_subscription_stub_view_model import EventSubscriptionStubViewModel
from plugins.model.event_subscription_update_args import EventSubscriptionUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_event_subscription_summary import PagingOfEventSubscriptionSummary


class EventSubscriptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.event_subscriptions_service_create_event_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (EventSubscriptionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions',
                'operation_id': 'event_subscriptions_service_create_event_subscription',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_subscription_create_args',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_subscription_create_args':
                        (EventSubscriptionCreateArgs,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'event_subscription_create_args': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.event_subscriptions_service_get_event_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (EventSubscriptionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions/{eventSubscriptionId}',
                'operation_id': 'event_subscriptions_service_get_event_subscription',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_subscription_id',
                ],
                'required': [
                    'event_subscription_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_subscription_id':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                },
                'attribute_map': {
                    'event_subscription_id': 'eventSubscriptionId',
                },
                'location_map': {
                    'event_subscription_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.event_subscriptions_service_get_subscription_entity_types_endpoint = _Endpoint(
            settings={
                'response_type': ([EntityTypeModel],),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions/event-types',
                'operation_id': 'event_subscriptions_service_get_subscription_entity_types',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.event_subscriptions_service_get_subscription_stub_endpoint = _Endpoint(
            settings={
                'response_type': (EventSubscriptionStubViewModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions/stub',
                'operation_id': 'event_subscriptions_service_get_subscription_stub',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.event_subscriptions_service_search_event_subscriptions_endpoint = _Endpoint(
            settings={
                'response_type': (PagingOfEventSubscriptionSummary,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions',
                'operation_id': 'event_subscriptions_service_search_event_subscriptions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_include_inactive',
                    'skip',
                    'sort_by_0_direction',
                    'sort_by_0_name',
                    'sort_by_0_priority',
                    'take',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'filter_include_inactive':
                        (bool,),
                    'skip':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'sort_by_0_direction':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'sort_by_0_name':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'sort_by_0_priority':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'take':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                },
                'attribute_map': {
                    'filter_include_inactive': 'filter.includeInactive',
                    'skip': 'skip',
                    'sort_by_0_direction': 'sortBy[0].direction',
                    'sort_by_0_name': 'sortBy[0].name',
                    'sort_by_0_priority': 'sortBy[0].priority',
                    'take': 'take',
                },
                'location_map': {
                    'filter_include_inactive': 'query',
                    'skip': 'query',
                    'sort_by_0_direction': 'query',
                    'sort_by_0_name': 'query',
                    'sort_by_0_priority': 'query',
                    'take': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.event_subscriptions_service_update_event_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (EventSubscriptionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/event-subscriptions/{eventSubscriptionId}',
                'operation_id': 'event_subscriptions_service_update_event_subscription',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_subscription_id',
                    'event_subscription_update_args',
                ],
                'required': [
                    'event_subscription_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_subscription_id':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'event_subscription_update_args':
                        (EventSubscriptionUpdateArgs,),
                },
                'attribute_map': {
                    'event_subscription_id': 'eventSubscriptionId',
                },
                'location_map': {
                    'event_subscription_id': 'path',
                    'event_subscription_update_args': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def event_subscriptions_service_create_event_subscription(
        self,
        **kwargs
    ):
        """Create event subscription  # noqa: E501

        Create a new event subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_create_event_subscription(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            event_subscription_create_args (EventSubscriptionCreateArgs): args. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EventSubscriptionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.event_subscriptions_service_create_event_subscription_endpoint.call_with_http_info(**kwargs)

    def event_subscriptions_service_get_event_subscription(
        self,
        event_subscription_id,
        **kwargs
    ):
        """event subscription  # noqa: E501

        Details for a specific event subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_get_event_subscription(event_subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_subscription_id (bool, date, datetime, dict, float, int, list, str, none_type): eventSubscriptionId

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EventSubscriptionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['event_subscription_id'] = \
            event_subscription_id
        return self.event_subscriptions_service_get_event_subscription_endpoint.call_with_http_info(**kwargs)

    def event_subscriptions_service_get_subscription_entity_types(
        self,
        **kwargs
    ):
        """Get an Event Subscription Types and Actions  # noqa: E501

        Returns the array of Event Subscription Types and Actions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_get_subscription_entity_types(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [EntityTypeModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.event_subscriptions_service_get_subscription_entity_types_endpoint.call_with_http_info(**kwargs)

    def event_subscriptions_service_get_subscription_stub(
        self,
        **kwargs
    ):
        """Get an empty event subscription  # noqa: E501

        Returns the empty event subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_get_subscription_stub(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EventSubscriptionStubViewModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.event_subscriptions_service_get_subscription_stub_endpoint.call_with_http_info(**kwargs)

    def event_subscriptions_service_search_event_subscriptions(
        self,
        **kwargs
    ):
        """Search event subscriptions  # noqa: E501

        Search, filter, sort, and page event subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_search_event_subscriptions(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_include_inactive (bool): IncludeInactive. [optional]
            skip (bool, date, datetime, dict, float, int, list, str, none_type): Number of records to skip before taking results. [optional]
            sort_by_0_direction (bool, date, datetime, dict, float, int, list, str, none_type): Sort direction. [optional]
            sort_by_0_name (bool, date, datetime, dict, float, int, list, str, none_type): Sort field name. [optional]
            sort_by_0_priority (bool, date, datetime, dict, float, int, list, str, none_type): Priority index. Sorts with lower values are executed earlier. [optional]
            take (bool, date, datetime, dict, float, int, list, str, none_type): Maximum number of records to include in results. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PagingOfEventSubscriptionSummary
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.event_subscriptions_service_search_event_subscriptions_endpoint.call_with_http_info(**kwargs)

    def event_subscriptions_service_update_event_subscription(
        self,
        event_subscription_id,
        **kwargs
    ):
        """Update event subscription  # noqa: E501

        Update an event subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_subscriptions_service_update_event_subscription(event_subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_subscription_id (bool, date, datetime, dict, float, int, list, str, none_type): eventSubscriptionId

        Keyword Args:
            event_subscription_update_args (EventSubscriptionUpdateArgs): args. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EventSubscriptionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['event_subscription_id'] = \
            event_subscription_id
        return self.event_subscriptions_service_update_event_subscription_endpoint.call_with_http_info(**kwargs)

