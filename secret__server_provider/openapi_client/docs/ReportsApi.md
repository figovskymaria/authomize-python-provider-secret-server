# plugins.ReportsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_service_create_report**](ReportsApi.md#reports_service_create_report) | **POST** /v1/reports | Create Report
[**reports_service_create_report_category**](ReportsApi.md#reports_service_create_report_category) | **POST** /v1/reports/categories | Create Report Category
[**reports_service_create_report_schedule**](ReportsApi.md#reports_service_create_report_schedule) | **POST** /v1/reports/schedules | Create Report Schedule
[**reports_service_delete**](ReportsApi.md#reports_service_delete) | **DELETE** /v1/reports/{id} | Delete Report
[**reports_service_delete_report_category**](ReportsApi.md#reports_service_delete_report_category) | **DELETE** /v1/reports/categories/{reportCategoryId} | Delete Report Category
[**reports_service_delete_report_category_v2**](ReportsApi.md#reports_service_delete_report_category_v2) | **DELETE** /v2/reports/categories/{reportCategoryId} | Delete Report Category
[**reports_service_delete_report_schedule**](ReportsApi.md#reports_service_delete_report_schedule) | **DELETE** /v1/reports/schedules/{reportScheduleId} | Delete Report Schedule
[**reports_service_delete_report_schedule_v2**](ReportsApi.md#reports_service_delete_report_schedule_v2) | **DELETE** /v2/reports/schedules/{reportScheduleId} | Delete Report Schedule
[**reports_service_delete_v2**](ReportsApi.md#reports_service_delete_v2) | **DELETE** /v2/reports/{id} | Delete Report
[**reports_service_download_historical_report**](ReportsApi.md#reports_service_download_historical_report) | **POST** /v1/reports/schedules/{reportScheduleHistoryId}/history/download | Download Historical Report
[**reports_service_email**](ReportsApi.md#reports_service_email) | **POST** /v1/reports/{id}/email | Email Report
[**reports_service_execute**](ReportsApi.md#reports_service_execute) | **POST** /v1/reports/execute | Execute Report
[**reports_service_export**](ReportsApi.md#reports_service_export) | **POST** /v1/reports/export | Export Report
[**reports_service_get_categories**](ReportsApi.md#reports_service_get_categories) | **GET** /v1/reports/categories | List Report Categories
[**reports_service_get_chart_types**](ReportsApi.md#reports_service_get_chart_types) | **GET** /v1/reports/charttypes | List Report Chart Types
[**reports_service_get_default_parameters**](ReportsApi.md#reports_service_get_default_parameters) | **GET** /v1/reports/{id}/defaultparameters | Report Parameters
[**reports_service_get_report_audits**](ReportsApi.md#reports_service_get_report_audits) | **GET** /v1/reports/audits | Get All Report Audits
[**reports_service_get_report_audits_by_id**](ReportsApi.md#reports_service_get_report_audits_by_id) | **GET** /v1/reports/{id}/audits | Get Report Audits
[**reports_service_get_report_category**](ReportsApi.md#reports_service_get_report_category) | **GET** /v1/reports/categories/{reportCategoryId} | Get Report Category
[**reports_service_get_report_category_permission_options**](ReportsApi.md#reports_service_get_report_category_permission_options) | **GET** /v1/reports/categories/permissions/options | Get Report Category Permission Options
[**reports_service_get_report_category_permissions**](ReportsApi.md#reports_service_get_report_category_permissions) | **GET** /v1/reports/categories/{reportCategoryId}/permissions | Get a Report Category&#39;s Permissions
[**reports_service_get_report_detail**](ReportsApi.md#reports_service_get_report_detail) | **GET** /v1/reports/{id} | Get Report
[**reports_service_get_report_permission_options**](ReportsApi.md#reports_service_get_report_permission_options) | **GET** /v1/reports/permissions/options | Get Report Permission Options
[**reports_service_get_report_permissions**](ReportsApi.md#reports_service_get_report_permissions) | **GET** /v1/reports/{reportId}/permissions | Get a Report&#39;s Permissions
[**reports_service_get_report_permissions_from_category**](ReportsApi.md#reports_service_get_report_permissions_from_category) | **GET** /v1/reports/{reportCategoryId}/permissions-from-category | Get a Report&#39;s Permissions from a Report Category
[**reports_service_get_report_schedule**](ReportsApi.md#reports_service_get_report_schedule) | **GET** /v1/reports/schedules/{reportScheduleId} | Get Report Schedule
[**reports_service_get_report_schedule_history**](ReportsApi.md#reports_service_get_report_schedule_history) | **GET** /v1/reports/schedules/{reportScheduleHistoryId}/history | Get Report Schedule History
[**reports_service_lookup**](ReportsApi.md#reports_service_lookup) | **GET** /v1/reports/lookup | Lookup Reports
[**reports_service_search_report_schedule_history**](ReportsApi.md#reports_service_search_report_schedule_history) | **GET** /v1/reports/schedules/{reportScheduleId}/history/search | Search Report Schedule History
[**reports_service_search_report_schedules**](ReportsApi.md#reports_service_search_report_schedules) | **GET** /v1/reports/schedules | Search Report Schedules
[**reports_service_search_report_summary**](ReportsApi.md#reports_service_search_report_summary) | **GET** /v1/reports | Search Reports
[**reports_service_stub_report_schedule**](ReportsApi.md#reports_service_stub_report_schedule) | **GET** /v1/reports/schedules/stub/{reportId} | Stub Report Schedule
[**reports_service_undelete_report_schedule**](ReportsApi.md#reports_service_undelete_report_schedule) | **PUT** /v1/reports/schedules/{reportScheduleId}/undelete | Undelete Report Schedule
[**reports_service_undelete_system_report**](ReportsApi.md#reports_service_undelete_system_report) | **PUT** /v1/reports/{reportId}/undelete | Undelete System Report
[**reports_service_update_report**](ReportsApi.md#reports_service_update_report) | **PUT** /v1/reports/{id} | Update Report
[**reports_service_update_report_category**](ReportsApi.md#reports_service_update_report_category) | **PATCH** /v1/reports/categories/{reportCategoryId} | Update Report Category
[**reports_service_update_report_category_permissions**](ReportsApi.md#reports_service_update_report_category_permissions) | **PATCH** /v1/reports/categories/{reportCategoryId}/permissions | Update Category Report Permissions
[**reports_service_update_report_permissions**](ReportsApi.md#reports_service_update_report_permissions) | **PATCH** /v1/reports/{reportId}/permissions | Update Report Permissions
[**reports_service_update_report_schedule**](ReportsApi.md#reports_service_update_report_schedule) | **PATCH** /v1/reports/schedules/{reportScheduleId} | Update Report Schedule


# **reports_service_create_report**
> ReportModel reports_service_create_report()

Create Report

Creates a new Report and returns the report

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.report_create_args import ReportCreateArgs
from plugins.model.report_model import ReportModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_create_args = ReportCreateArgs(
        category_id=None,
        chart_type=None,
        description=None,
        dual_control_approval=DualControlApproval(
            domain_id=None,
            password=None,
            two_factor=None,
            username=None,
        ),
        is3_d_report=True,
        name=None,
        page_size=None,
        report_sql=None,
        use_database_paging=True,
    ) # ReportCreateArgs | Report create options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Report
        api_response = api_instance.reports_service_create_report(report_create_args=report_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_create_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_create_args** | [**ReportCreateArgs**](ReportCreateArgs.md)| Report create options | [optional]

### Return type

[**ReportModel**](ReportModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_create_report_category**
> ReportCategoryDetailModel reports_service_create_report_category()

Create Report Category

Create Report Category

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_category_detail_model import ReportCategoryDetailModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_category_create_args import ReportCategoryCreateArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_create_args = ReportCategoryCreateArgs(
        data=ReportCategoryCreateModel(
            report_category_description=None,
            report_category_name=None,
            sort_order=None,
        ),
    ) # ReportCategoryCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Report Category
        api_response = api_instance.reports_service_create_report_category(report_category_create_args=report_category_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_create_report_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_create_args** | [**ReportCategoryCreateArgs**](ReportCategoryCreateArgs.md)| args | [optional]

### Return type

[**ReportCategoryDetailModel**](ReportCategoryDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_create_report_schedule**
> ReportScheduleModel reports_service_create_report_schedule()

Create Report Schedule

Create Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_schedule_model import ReportScheduleModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_schedule_create_args import ReportScheduleCreateArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_create_args = ReportScheduleCreateArgs(
        data=ReportScheduleCreateModel(
            custom_parameter_value=None,
            end_date_parameter_specific_date_value=None,
            end_date_parameter_value=None,
            folder_parameter_value=None,
            group_parameter_value=None,
            report_id=None,
            schedule=ScheduleCreateModel(
                additional_email_addresses=None,
                change_type=ScheduleChangeType("{}"),
                days=None,
                email_groups=[
                    None,
                ],
                friday=True,
                health_check=True,
                history_size=None,
                monday=True,
                monthly_day=None,
                monthly_day_of_month=None,
                monthly_day_order=None,
                monthly_day_order_recurrence=None,
                monthly_day_recurrence=None,
                monthly_schedule_type=None,
                saturday=True,
                schedule_name=None,
                send_email=True,
                send_email_with_high_priority=True,
                starting_on=None,
                sunday=True,
                thursday=True,
                tuesday=True,
                wednesday=True,
                weeks=None,
            ),
            start_date_parameter_specific_date_value=None,
            start_date_parameter_value=None,
            user_parameter_value=None,
        ),
    ) # ReportScheduleCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Report Schedule
        api_response = api_instance.reports_service_create_report_schedule(report_schedule_create_args=report_schedule_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_create_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_create_args** | [**ReportScheduleCreateArgs**](ReportScheduleCreateArgs.md)| args | [optional]

### Return type

[**ReportScheduleModel**](ReportScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete**
> bool reports_service_delete(id)

Delete Report

Delete a report by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Report
        api_response = api_instance.reports_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report ID |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete_report_category**
> bool reports_service_delete_report_category(report_category_id)

Delete Report Category

This will delete the report category and all assigned reports will be set inactive

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId

    # example passing only required values which don't have defaults set
    try:
        # Delete Report Category
        api_response = api_instance.reports_service_delete_report_category(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete_report_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | true if success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete_report_category_v2**
> DeletedModel reports_service_delete_report_category_v2(report_category_id)

Delete Report Category

This will delete the report category and all assigned reports will be set inactive

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId

    # example passing only required values which don't have defaults set
    try:
        # Delete Report Category
        api_response = api_instance.reports_service_delete_report_category_v2(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete_report_category_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |

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
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete_report_schedule**
> bool reports_service_delete_report_schedule(report_schedule_id)

Delete Report Schedule

Delete Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId

    # example passing only required values which don't have defaults set
    try:
        # Delete Report Schedule
        api_response = api_instance.reports_service_delete_report_schedule(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete_report_schedule_v2**
> DeletedModel reports_service_delete_report_schedule_v2(report_schedule_id)

Delete Report Schedule

Delete Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId

    # example passing only required values which don't have defaults set
    try:
        # Delete Report Schedule
        api_response = api_instance.reports_service_delete_report_schedule_v2(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete_report_schedule_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |

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
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_delete_v2**
> DeletedModel reports_service_delete_v2(id)

Delete Report

Delete a report by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Report
        api_response = api_instance.reports_service_delete_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_delete_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report ID |

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
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_download_historical_report**
> HttpResponseMessage reports_service_download_historical_report(report_schedule_history_id)

Download Historical Report

Download historical report from a schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.http_response_message import HttpResponseMessage
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_history_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleHistoryId

    # example passing only required values which don't have defaults set
    try:
        # Download Historical Report
        api_response = api_instance.reports_service_download_historical_report(report_schedule_history_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_download_historical_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_history_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleHistoryId |

### Return type

[**HttpResponseMessage**](HttpResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_email**
> ReportEmailResponse reports_service_email(id)

Email Report

Email a report

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_email_response import ReportEmailResponse
from plugins.model.report_email_args import ReportEmailArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report Id
    report_email_args = ReportEmailArgs(
        data=ReportEmailModel(
            email_address=None,
            format=ReportFormat("{}"),
            parameters=[
                ReportParameterValue(
                    name=None,
                    value={},
                    value_display_name=None,
                ),
            ],
        ),
    ) # ReportEmailArgs | Report email options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Email Report
        api_response = api_instance.reports_service_email(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Email Report
        api_response = api_instance.reports_service_email(id, report_email_args=report_email_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report Id |
 **report_email_args** | [**ReportEmailArgs**](ReportEmailArgs.md)| Report email options | [optional]

### Return type

[**ReportEmailResponse**](ReportEmailResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object email result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_execute**
> ReportExecuteModel reports_service_execute()

Execute Report

Executes a Report and returns the results

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_execute_model import ReportExecuteModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_execute_args import ReportExecuteArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_execute_args = ReportExecuteArgs(
        dual_control_approval=DualControlApproval(
            domain_id=None,
            password=None,
            two_factor=None,
            username=None,
        ),
        encode_html=True,
        end_record_number=None,
        id=None,
        is_ascending=True,
        name=None,
        order_by_field_ordinal=None,
        page_number=None,
        parameters=[
            ReportParameter(
                name=None,
                value=None,
            ),
        ],
        preview_sql=None,
        records_per_page=None,
        start_record_number=None,
        use_default_parameters=True,
    ) # ReportExecuteArgs | Report execute options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Report
        api_response = api_instance.reports_service_execute(report_execute_args=report_execute_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_execute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_execute_args** | [**ReportExecuteArgs**](ReportExecuteArgs.md)| Report execute options | [optional]

### Return type

[**ReportExecuteModel**](ReportExecuteModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_export**
> bool, date, datetime, dict, float, int, list, str, none_type reports_service_export()

Export Report

Exports a Report and returns the results

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.report_export_args import ReportExportArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_export_args = ReportExportArgs(
        delimiter=None,
        dual_control_approval=DualControlApproval(
            domain_id=None,
            password=None,
            two_factor=None,
            username=None,
        ),
        encode_html=True,
        end_record_number=None,
        format=None,
        id=None,
        is_ascending=True,
        name=None,
        order_by_field_ordinal=None,
        page_number=None,
        parameters=[
            ReportParameter(
                name=None,
                value=None,
            ),
        ],
        preview_sql=None,
        records_per_page=None,
        start_record_number=None,
        time_zone=None,
        use_default_parameters=True,
    ) # ReportExportArgs | Report execute options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Report
        api_response = api_instance.reports_service_export(report_export_args=report_export_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_export_args** | [**ReportExportArgs**](ReportExportArgs.md)| Report execute options | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_categories**
> [ReportCategory] reports_service_get_categories()

List Report Categories

List the report categories

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_category import ReportCategory
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
    api_instance = reports_api.ReportsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Report Categories
        api_response = api_instance.reports_service_get_categories()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_categories: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ReportCategory]**](ReportCategory.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report categories array |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_chart_types**
> [ReportChartType] reports_service_get_chart_types()

List Report Chart Types

List the report chart types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.report_chart_type import ReportChartType
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
    api_instance = reports_api.ReportsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Report Chart Types
        api_response = api_instance.reports_service_get_chart_types()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_chart_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ReportChartType]**](ReportChartType.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report chart types array |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_default_parameters**
> ReportDefaultParams reports_service_get_default_parameters(id)

Report Parameters

Gets the default parameters for the specified report

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_default_params import ReportDefaultParams
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report ID

    # example passing only required values which don't have defaults set
    try:
        # Report Parameters
        api_response = api_instance.reports_service_get_default_parameters(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_default_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report ID |

### Return type

[**ReportDefaultParams**](ReportDefaultParams.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Parameters |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_audits**
> PagingOfReportAuditSummary reports_service_get_report_audits()

Get All Report Audits

Get all report audits

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.paging_of_report_audit_summary import PagingOfReportAuditSummary
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
    api_instance = reports_api.ReportsApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Report Audits
        api_response = api_instance.reports_service_get_report_audits(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfReportAuditSummary**](PagingOfReportAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Audit Summaries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_audits_by_id**
> PagingOfReportAuditSummary reports_service_get_report_audits_by_id(id)

Get Report Audits

Get report audits by report Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.paging_of_report_audit_summary import PagingOfReportAuditSummary
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Report Audits
        api_response = api_instance.reports_service_get_report_audits_by_id(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_audits_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Report Audits
        api_response = api_instance.reports_service_get_report_audits_by_id(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_audits_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfReportAuditSummary**](PagingOfReportAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Audit Summaries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_category**
> ReportCategoryDetailModel reports_service_get_report_category(report_category_id)

Get Report Category

Get Report Category

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_category_detail_model import ReportCategoryDetailModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId

    # example passing only required values which don't have defaults set
    try:
        # Get Report Category
        api_response = api_instance.reports_service_get_report_category(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |

### Return type

[**ReportCategoryDetailModel**](ReportCategoryDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_category_permission_options**
> [ReportCategoryPermissionOptionModel] reports_service_get_report_category_permission_options()

Get Report Category Permission Options

Get Report Category Permission Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_category_permission_option_model import ReportCategoryPermissionOptionModel
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
    api_instance = reports_api.ReportsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Report Category Permission Options
        api_response = api_instance.reports_service_get_report_category_permission_options()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_category_permission_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ReportCategoryPermissionOptionModel]**](ReportCategoryPermissionOptionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category Permissions Options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_category_permissions**
> IPagingOfReportCategoryPermissionModel reports_service_get_report_category_permissions(report_category_id)

Get a Report Category's Permissions

Get a Report Category's Permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_category_permission_model import IPagingOfReportCategoryPermissionModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Report Category's Permissions
        api_response = api_instance.reports_service_get_report_category_permissions(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_category_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Report Category's Permissions
        api_response = api_instance.reports_service_get_report_category_permissions(report_category_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_category_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfReportCategoryPermissionModel**](IPagingOfReportCategoryPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category Permissions for a Report Category |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_detail**
> ReportModel reports_service_get_report_detail(id)

Get Report

Gets a Report and returns the Report Model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.report_model import ReportModel
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report ID

    # example passing only required values which don't have defaults set
    try:
        # Get Report
        api_response = api_instance.reports_service_get_report_detail(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report ID |

### Return type

[**ReportModel**](ReportModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_permission_options**
> [ReportPermissionOptionModel] reports_service_get_report_permission_options()

Get Report Permission Options

Get Report Permission Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_permission_option_model import ReportPermissionOptionModel
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
    api_instance = reports_api.ReportsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Report Permission Options
        api_response = api_instance.reports_service_get_report_permission_options()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_permission_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ReportPermissionOptionModel]**](ReportPermissionOptionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Permissions Options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_permissions**
> IPagingOfReportPermissionModel reports_service_get_report_permissions(report_id)

Get a Report's Permissions

Get a Report's Permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_permission_model import IPagingOfReportPermissionModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Report's Permissions
        api_response = api_instance.reports_service_get_report_permissions(report_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Report's Permissions
        api_response = api_instance.reports_service_get_report_permissions(report_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfReportPermissionModel**](IPagingOfReportPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Permissions for a Report |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_permissions_from_category**
> IPagingOfReportPermissionModel reports_service_get_report_permissions_from_category(report_category_id)

Get a Report's Permissions from a Report Category

Get a Report's Permissions from a Report Category

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_permission_model import IPagingOfReportPermissionModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Report's Permissions from a Report Category
        api_response = api_instance.reports_service_get_report_permissions_from_category(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_permissions_from_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Report's Permissions from a Report Category
        api_response = api_instance.reports_service_get_report_permissions_from_category(report_category_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_permissions_from_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfReportPermissionModel**](IPagingOfReportPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Permissions for a Report from a Report Category |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_schedule**
> ReportScheduleModel reports_service_get_report_schedule(report_schedule_id)

Get Report Schedule

Get Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_schedule_model import ReportScheduleModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId

    # example passing only required values which don't have defaults set
    try:
        # Get Report Schedule
        api_response = api_instance.reports_service_get_report_schedule(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |

### Return type

[**ReportScheduleModel**](ReportScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_get_report_schedule_history**
> IPagingOfReportScheduleHistorySummaryModel reports_service_get_report_schedule_history(report_schedule_history_id)

Get Report Schedule History

Get a Report Schedule History

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_schedule_history_summary_model import IPagingOfReportScheduleHistorySummaryModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_history_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleHistoryId

    # example passing only required values which don't have defaults set
    try:
        # Get Report Schedule History
        api_response = api_instance.reports_service_get_report_schedule_history(report_schedule_history_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_get_report_schedule_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_history_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleHistoryId |

### Return type

[**IPagingOfReportScheduleHistorySummaryModel**](IPagingOfReportScheduleHistorySummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule History for a ScheduleReportHistoryId |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_lookup**
> PagingOfReportLookup reports_service_lookup()

Lookup Reports

Search, filter, sort, and page reports, returning only group ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_report_lookup import PagingOfReportLookup
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
    api_instance = reports_api.ReportsApi(api_client)
    filter_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Category ID (optional)
    filter_include_inactive = True # bool | Whether to include inactive Reports in the results (optional)
    filter_report_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Report Name - Searching by report name ignores other filters (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Reports
        api_response = api_instance.reports_service_lookup(filter_category_id=filter_category_id, filter_include_inactive=filter_include_inactive, filter_report_name=filter_report_name, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Category ID | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive Reports in the results | [optional]
 **filter_report_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report Name - Searching by report name ignores other filters | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfReportLookup**](PagingOfReportLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reports search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_search_report_schedule_history**
> IPagingOfReportScheduleHistorySummaryModel reports_service_search_report_schedule_history(report_schedule_id)

Search Report Schedule History

Search Report Schedule History

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_schedule_history_summary_model import IPagingOfReportScheduleHistorySummaryModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Report Schedule History
        api_response = api_instance.reports_service_search_report_schedule_history(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_search_report_schedule_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Report Schedule History
        api_response = api_instance.reports_service_search_report_schedule_history(report_schedule_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_search_report_schedule_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfReportScheduleHistorySummaryModel**](IPagingOfReportScheduleHistorySummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule History for a particular Id |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_search_report_schedules**
> IPagingOfReportScheduleSummaryModel reports_service_search_report_schedules()

Search Report Schedules

Search Report Schedules

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_report_schedule_summary_model import IPagingOfReportScheduleSummaryModel
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
    api_instance = reports_api.ReportsApi(api_client)
    filter_include_deleted = True # bool | When set, deleted reports will be included (optional)
    filter_report_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report Id (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Report Schedules
        api_response = api_instance.reports_service_search_report_schedules(filter_include_deleted=filter_include_deleted, filter_report_id=filter_report_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_search_report_schedules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_deleted** | **bool**| When set, deleted reports will be included | [optional]
 **filter_report_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report Id | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfReportScheduleSummaryModel**](IPagingOfReportScheduleSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedules that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_search_report_summary**
> PagingOfReportSummary reports_service_search_report_summary()

Search Reports

Search, filter, sort, and page reports

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_report_summary import PagingOfReportSummary
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
    api_instance = reports_api.ReportsApi(api_client)
    filter_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Category ID (optional)
    filter_include_inactive = True # bool | Whether to include inactive Reports in the results (optional)
    filter_report_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Report Name - Searching by report name ignores other filters (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Reports
        api_response = api_instance.reports_service_search_report_summary(filter_category_id=filter_category_id, filter_include_inactive=filter_include_inactive, filter_report_name=filter_report_name, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_search_report_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Category ID | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive Reports in the results | [optional]
 **filter_report_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report Name - Searching by report name ignores other filters | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfReportSummary**](PagingOfReportSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_stub_report_schedule**
> ReportScheduleModel reports_service_stub_report_schedule(report_id)

Stub Report Schedule

Stub Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_schedule_model import ReportScheduleModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportId

    # example passing only required values which don't have defaults set
    try:
        # Stub Report Schedule
        api_response = api_instance.reports_service_stub_report_schedule(report_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_stub_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportId |

### Return type

[**ReportScheduleModel**](ReportScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_undelete_report_schedule**
> bool reports_service_undelete_report_schedule(report_schedule_id)

Undelete Report Schedule

Undelete Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId

    # example passing only required values which don't have defaults set
    try:
        # Undelete Report Schedule
        api_response = api_instance.reports_service_undelete_report_schedule(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_undelete_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_undelete_system_report**
> UndeleteReportResponse reports_service_undelete_system_report(report_id)

Undelete System Report

Allows user to undelete system reports only.  Non-system reports are required to be edited in order for the SQL to be valdiated properly.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.undelete_report_response import UndeleteReportResponse
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportId

    # example passing only required values which don't have defaults set
    try:
        # Undelete System Report
        api_response = api_instance.reports_service_undelete_system_report(report_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_undelete_system_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportId |

### Return type

[**UndeleteReportResponse**](UndeleteReportResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns success/fail model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_update_report**
> ReportModel reports_service_update_report(id)

Update Report

Updates a Report and returns the report

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.report_model import ReportModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_update_args import ReportUpdateArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Report ID
    report_update_args = ReportUpdateArgs(
        category_id=None,
        chart_type=None,
        description=None,
        dual_control_approval=DualControlApproval(
            domain_id=None,
            password=None,
            two_factor=None,
            username=None,
        ),
        id=None,
        is3_d_report=True,
        name=None,
        page_size=None,
        report_sql=None,
        use_database_paging=True,
    ) # ReportUpdateArgs | Report update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Report
        api_response = api_instance.reports_service_update_report(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Report
        api_response = api_instance.reports_service_update_report(id, report_update_args=report_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Report ID |
 **report_update_args** | [**ReportUpdateArgs**](ReportUpdateArgs.md)| Report update options | [optional]

### Return type

[**ReportModel**](ReportModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_update_report_category**
> ReportCategoryDetailModel reports_service_update_report_category(report_category_id)

Update Report Category

Update Report Category

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_category_detail_model import ReportCategoryDetailModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_category_update_args import ReportCategoryUpdateArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId
    report_category_update_args = ReportCategoryUpdateArgs(
        data=ReportCategoryUpdateModel(
            report_category_description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            report_category_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # ReportCategoryUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Report Category
        api_response = api_instance.reports_service_update_report_category(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Report Category
        api_response = api_instance.reports_service_update_report_category(report_category_id, report_category_update_args=report_category_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |
 **report_category_update_args** | [**ReportCategoryUpdateArgs**](ReportCategoryUpdateArgs.md)| args | [optional]

### Return type

[**ReportCategoryDetailModel**](ReportCategoryDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_update_report_category_permissions**
> IPagingOfReportCategoryPermissionModel reports_service_update_report_category_permissions(report_category_id)

Update Category Report Permissions

Update Category Report Permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_category_permissions_update_args import ReportCategoryPermissionsUpdateArgs
from plugins.model.i_paging_of_report_category_permission_model import IPagingOfReportCategoryPermissionModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_category_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportCategoryId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)
    report_category_permissions_update_args = ReportCategoryPermissionsUpdateArgs(
        data=ReportCategoryPermissionsUpdateModel(
            allow_remove_edit=True,
            permissions=UpdateFieldValueOfReportCategoryPermissionUpdateModelArray(
                dirty=True,
                value=[
                    ReportCategoryPermissionUpdateModel(
                        group_id=None,
                        role_permission_id=None,
                    ),
                ],
            ),
        ),
    ) # ReportCategoryPermissionsUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Category Report Permissions
        api_response = api_instance.reports_service_update_report_category_permissions(report_category_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_category_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Category Report Permissions
        api_response = api_instance.reports_service_update_report_category_permissions(report_category_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take, report_category_permissions_update_args=report_category_permissions_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_category_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportCategoryId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]
 **report_category_permissions_update_args** | [**ReportCategoryPermissionsUpdateArgs**](ReportCategoryPermissionsUpdateArgs.md)| args | [optional]

### Return type

[**IPagingOfReportCategoryPermissionModel**](IPagingOfReportCategoryPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Category Permissions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_update_report_permissions**
> IPagingOfReportPermissionModel reports_service_update_report_permissions(report_id)

Update Report Permissions

Update Report Permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_permissions_update_args import ReportPermissionsUpdateArgs
from plugins.model.i_paging_of_report_permission_model import IPagingOfReportPermissionModel
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportId
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)
    report_permissions_update_args = ReportPermissionsUpdateArgs(
        data=ReportPermissionsUpdateModel(
            allow_remove_edit=True,
            enable_inherit_permissions=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            permissions=UpdateFieldValueOfReportPermissionUpdateModelArray(
                dirty=True,
                value=[
                    ReportPermissionUpdateModel(
                        group_id=None,
                        role_permission_id=None,
                    ),
                ],
            ),
        ),
    ) # ReportPermissionsUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Report Permissions
        api_response = api_instance.reports_service_update_report_permissions(report_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Report Permissions
        api_response = api_instance.reports_service_update_report_permissions(report_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take, report_permissions_update_args=report_permissions_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportId |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]
 **report_permissions_update_args** | [**ReportPermissionsUpdateArgs**](ReportPermissionsUpdateArgs.md)| args | [optional]

### Return type

[**IPagingOfReportPermissionModel**](IPagingOfReportPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Permissions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_service_update_report_schedule**
> ReportScheduleModel reports_service_update_report_schedule(report_schedule_id)

Update Report Schedule

Update Report Schedule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import reports_api
from plugins.model.report_schedule_model import ReportScheduleModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.report_schedule_update_args import ReportScheduleUpdateArgs
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
    api_instance = reports_api.ReportsApi(api_client)
    report_schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | reportScheduleId
    report_schedule_update_args = ReportScheduleUpdateArgs(
        data=ReportScheduleUpdateModel(
            custom_parameter_value=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            end_date_parameter_specific_date_value=UpdateFieldValueOfOptionalDateTime(
                dirty=True,
                value=None,
            ),
            end_date_parameter_value=UpdateFieldValueOfOptionalReportScheduleDateParameterType(
                dirty=True,
                value=None,
            ),
            folder_parameter_value=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            format=UpdateFieldValueOfReportFormat(
                dirty=True,
                value=ReportFormat("{}"),
            ),
            group_parameter_value=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            schedule=ScheduleUpdateModel(
                additional_email_addresses=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                change_type=UpdateFieldValueOfScheduleChangeType(
                    dirty=True,
                    value=ScheduleChangeType("{}"),
                ),
                days=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                email_groups=UpdateFieldValueOfInt32Array(
                    dirty=True,
                    value=[
                        None,
                    ],
                ),
                friday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                health_check=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                history_size=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                monday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                monthly_day=UpdateFieldValueOfOptionalScheduleMonthlyDayType(
                    dirty=True,
                    value=None,
                ),
                monthly_day_of_month=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                monthly_day_order=UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType(
                    dirty=True,
                    value=None,
                ),
                monthly_day_order_recurrence=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                monthly_day_recurrence=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                monthly_schedule_type=UpdateFieldValueOfOptionalScheduleMonthlyType(
                    dirty=True,
                    value=None,
                ),
                saturday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                schedule_name=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                send_email=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                send_email_with_high_priority=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                starting_on=UpdateFieldValueOfDateTime(
                    dirty=True,
                    value=None,
                ),
                sunday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                thursday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                tuesday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                wednesday=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                weeks=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
            ),
            start_date_parameter_specific_date_value=UpdateFieldValueOfOptionalDateTime(
                dirty=True,
                value=None,
            ),
            start_date_parameter_value=UpdateFieldValueOfOptionalReportScheduleDateParameterType(
                dirty=True,
                value=None,
            ),
            user_parameter_value=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # ReportScheduleUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Report Schedule
        api_response = api_instance.reports_service_update_report_schedule(report_schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_schedule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Report Schedule
        api_response = api_instance.reports_service_update_report_schedule(report_schedule_id, report_schedule_update_args=report_schedule_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ReportsApi->reports_service_update_report_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| reportScheduleId |
 **report_schedule_update_args** | [**ReportScheduleUpdateArgs**](ReportScheduleUpdateArgs.md)| args | [optional]

### Return type

[**ReportScheduleModel**](ReportScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report Schedule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

