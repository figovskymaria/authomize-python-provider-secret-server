# plugins.RemotePasswordChangingApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_password_changing_service_create_custom_command**](RemotePasswordChangingApi.md#remote_password_changing_service_create_custom_command) | **POST** /v1/remote-password-changing/custom-commands | Create Custom Command
[**remote_password_changing_service_create_password_type**](RemotePasswordChangingApi.md#remote_password_changing_service_create_password_type) | **POST** /v1/remote-password-changing/password-types | Create Password Type
[**remote_password_changing_service_delete_custom_command**](RemotePasswordChangingApi.md#remote_password_changing_service_delete_custom_command) | **DELETE** /v1/remote-password-changing/custom-commands/{id} | Delete Custom Command
[**remote_password_changing_service_delete_password_type**](RemotePasswordChangingApi.md#remote_password_changing_service_delete_password_type) | **DELETE** /v1/remote-password-changing/password-types/{id} | Delete Password Type
[**remote_password_changing_service_get_custom_commands**](RemotePasswordChangingApi.md#remote_password_changing_service_get_custom_commands) | **GET** /v1/remote-password-changing/custom-commands/{id} | Custom Command List
[**remote_password_changing_service_get_password_type**](RemotePasswordChangingApi.md#remote_password_changing_service_get_password_type) | **GET** /v1/remote-password-changing/password-types/{id} | Password Type By Id
[**remote_password_changing_service_get_password_type_list**](RemotePasswordChangingApi.md#remote_password_changing_service_get_password_type_list) | **GET** /v1/remote-password-changing/password-types | Password Type List
[**remote_password_changing_service_update_custom_command**](RemotePasswordChangingApi.md#remote_password_changing_service_update_custom_command) | **PUT** /v1/remote-password-changing/custom-commands/{id} | Update Custom Command
[**remote_password_changing_service_update_password_type**](RemotePasswordChangingApi.md#remote_password_changing_service_update_password_type) | **PUT** /v1/remote-password-changing/password-types/{id} | Update Password Type


# **remote_password_changing_service_create_custom_command**
> CustomCommandModel remote_password_changing_service_create_custom_command()

Create Custom Command

Create a New Custom Command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.custom_command_model import CustomCommandModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.custom_command_create_args import CustomCommandCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    custom_command_create_args = CustomCommandCreateArgs(
        command=None,
        command_type_code=None,
        comment=None,
        password_type_id=None,
        pause=None,
    ) # CustomCommandCreateArgs | Custom Command creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Custom Command
        api_response = api_instance.remote_password_changing_service_create_custom_command(custom_command_create_args=custom_command_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_create_custom_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_command_create_args** | [**CustomCommandCreateArgs**](CustomCommandCreateArgs.md)| Custom Command creation options | [optional]

### Return type

[**CustomCommandModel**](CustomCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created Custom Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_create_password_type**
> PasswordTypeModel remote_password_changing_service_create_password_type()

Create Password Type

Create a New Password Type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.password_type_create_args import PasswordTypeCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_type_model import PasswordTypeModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    password_type_create_args = PasswordTypeCreateArgs(
        base_password_type_id=None,
        name=None,
    ) # PasswordTypeCreateArgs | Password Type creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Password Type
        api_response = api_instance.remote_password_changing_service_create_password_type(password_type_create_args=password_type_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_create_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_type_create_args** | [**PasswordTypeCreateArgs**](PasswordTypeCreateArgs.md)| Password Type creation options | [optional]

### Return type

[**PasswordTypeModel**](PasswordTypeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created Password Type |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_delete_custom_command**
> DeletedModel remote_password_changing_service_delete_custom_command(id)

Delete Custom Command

Delete a Custom Command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Custom Command Id

    # example passing only required values which don't have defaults set
    try:
        # Delete Custom Command
        api_response = api_instance.remote_password_changing_service_delete_custom_command(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_delete_custom_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Custom Command Id |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete Password Custom Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_delete_password_type**
> DeletedModel remote_password_changing_service_delete_password_type(id)

Delete Password Type

Delete a Password Type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Password Type Id

    # example passing only required values which don't have defaults set
    try:
        # Delete Password Type
        api_response = api_instance.remote_password_changing_service_delete_password_type(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_delete_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Password Type Id |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete Password Type Response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_get_custom_commands**
> PagingOfCustomCommandModel remote_password_changing_service_get_custom_commands(id)

Custom Command List

Lists Available Custom Command for Password Type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.paging_of_custom_command_model import PagingOfCustomCommandModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Password Type Id
    filter_command_type_code = None # bool, date, datetime, dict, float, int, list, str, none_type | CommandTypeCode (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Custom Command List
        api_response = api_instance.remote_password_changing_service_get_custom_commands(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_get_custom_commands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Custom Command List
        api_response = api_instance.remote_password_changing_service_get_custom_commands(id, filter_command_type_code=filter_command_type_code, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_get_custom_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Password Type Id |
 **filter_command_type_code** | **bool, date, datetime, dict, float, int, list, str, none_type**| CommandTypeCode | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfCustomCommandModel**](PagingOfCustomCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Command List result for Password Type |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_get_password_type**
> PasswordTypeModel remote_password_changing_service_get_password_type(id)

Password Type By Id

Gets Password Type By Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_type_model import PasswordTypeModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Password Type Id

    # example passing only required values which don't have defaults set
    try:
        # Password Type By Id
        api_response = api_instance.remote_password_changing_service_get_password_type(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_get_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Password Type Id |

### Return type

[**PasswordTypeModel**](PasswordTypeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PasswordType |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_get_password_type_list**
> PagingOfPasswordTypeSummary remote_password_changing_service_get_password_type_list()

Password Type List

Lists Available Password Types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_password_type_summary import PagingOfPasswordTypeSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive Password Types in the results (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchTerm (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Password Type List
        api_response = api_instance.remote_password_changing_service_get_password_type_list(filter_include_inactive=filter_include_inactive, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_get_password_type_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive Password Types in the results | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchTerm | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfPasswordTypeSummary**](PagingOfPasswordTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PasswordType List result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_update_custom_command**
> CustomCommandModel remote_password_changing_service_update_custom_command(id)

Update Custom Command

Update a Custom Command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.custom_command_model import CustomCommandModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.custom_command_update_args import CustomCommandUpdateArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Custom Command Id
    custom_command_update_args = CustomCommandUpdateArgs(
        command=None,
        command_type_code=None,
        comment=None,
        concurrency_id=None,
        order=None,
        password_type_id=None,
        pause=None,
    ) # CustomCommandUpdateArgs | Custom Command update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Custom Command
        api_response = api_instance.remote_password_changing_service_update_custom_command(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_update_custom_command: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Custom Command
        api_response = api_instance.remote_password_changing_service_update_custom_command(id, custom_command_update_args=custom_command_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_update_custom_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Custom Command Id |
 **custom_command_update_args** | [**CustomCommandUpdateArgs**](CustomCommandUpdateArgs.md)| Custom Command update options | [optional]

### Return type

[**CustomCommandModel**](CustomCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Custom Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_password_changing_service_update_password_type**
> PasswordTypeModel remote_password_changing_service_update_password_type(id)

Update Password Type

Update a Password Type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import remote_password_changing_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_type_update_args import PasswordTypeUpdateArgs
from plugins.model.password_type_model import PasswordTypeModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_password_changing_api.RemotePasswordChangingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Password Type Id
    password_type_update_args = PasswordTypeUpdateArgs(
        active=True,
        can_edit=True,
        custom_port=None,
        exit_command=None,
        has_commands=True,
        heartbeat_script_args=None,
        heartbeat_script_id=None,
        ignore_ssl=True,
        is_web=True,
        ldap_connection_settings_id=None,
        line_ending=LineEnding("{}"),
        mainframe_connection_string=None,
        name=None,
        odbc_connection_string=None,
        rpc_script_args=None,
        rpc_script_id=None,
        runner_type=RunnerType("{}"),
        scan_item_template_id=None,
        use_ssl=True,
        use_username_and_password=True,
        valid_for_takeover=True,
        windows_custom_ports=None,
    ) # PasswordTypeUpdateArgs | Password Type update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Password Type
        api_response = api_instance.remote_password_changing_service_update_password_type(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_update_password_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Password Type
        api_response = api_instance.remote_password_changing_service_update_password_type(id, password_type_update_args=password_type_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RemotePasswordChangingApi->remote_password_changing_service_update_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Password Type Id |
 **password_type_update_args** | [**PasswordTypeUpdateArgs**](PasswordTypeUpdateArgs.md)| Password Type update options | [optional]

### Return type

[**PasswordTypeModel**](PasswordTypeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Password Type |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

