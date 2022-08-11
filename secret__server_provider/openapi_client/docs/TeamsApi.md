# plugins.TeamsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_service_add_lists_to_team**](TeamsApi.md#teams_service_add_lists_to_team) | **POST** /v1/teams/{id}/lists | Update Team Lists
[**teams_service_add_team_member**](TeamsApi.md#teams_service_add_team_member) | **POST** /v1/teams/{id}/members | Update Team Members
[**teams_service_add_team_site**](TeamsApi.md#teams_service_add_team_site) | **POST** /v1/teams/{id}/sites | Update Team Sites
[**teams_service_create_team**](TeamsApi.md#teams_service_create_team) | **POST** /v1/teams | Create Team
[**teams_service_get**](TeamsApi.md#teams_service_get) | **GET** /v1/teams/{id} | Get Team
[**teams_service_get_team_audits**](TeamsApi.md#teams_service_get_team_audits) | **GET** /v1/teams/{id}/audits | Get Team Audits
[**teams_service_get_team_lists**](TeamsApi.md#teams_service_get_team_lists) | **GET** /v1/teams/{id}/lists | Get a Team&#39;s Lists
[**teams_service_get_team_members**](TeamsApi.md#teams_service_get_team_members) | **GET** /v1/teams/{id}/members | Get Users In Team
[**teams_service_get_team_sites**](TeamsApi.md#teams_service_get_team_sites) | **GET** /v1/teams/{id}/sites | Get Sites for a Team
[**teams_service_search**](TeamsApi.md#teams_service_search) | **GET** /v1/teams | Search Teams
[**teams_service_stub**](TeamsApi.md#teams_service_stub) | **GET** /v1/teams/stub | Get Team Stub
[**teams_service_update_team**](TeamsApi.md#teams_service_update_team) | **PUT** /v1/teams/{id} | Update Team


# **teams_service_add_lists_to_team**
> TeamCategorizedListSummary teams_service_add_lists_to_team(id)

Update Team Lists

Save lists of the Team by ListId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_categorized_list_summary import TeamCategorizedListSummary
from plugins.model.team_categorized_list_update_args import TeamCategorizedListUpdateArgs
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team Id
    team_categorized_list_update_args = TeamCategorizedListUpdateArgs(
        list_ids=UpdateFieldValueOfGuidArray(
            dirty=True,
            value=[
                None,
            ],
        ),
        should_restrict_lists=UpdateFieldValueOfOptionalBoolean(
            dirty=True,
            value=True,
        ),
    ) # TeamCategorizedListUpdateArgs | Team list (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Team Lists
        api_response = api_instance.teams_service_add_lists_to_team(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_lists_to_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Team Lists
        api_response = api_instance.teams_service_add_lists_to_team(id, team_categorized_list_update_args=team_categorized_list_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_lists_to_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team Id |
 **team_categorized_list_update_args** | [**TeamCategorizedListUpdateArgs**](TeamCategorizedListUpdateArgs.md)| Team list | [optional]

### Return type

[**TeamCategorizedListSummary**](TeamCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary a Team&#39;s Lists. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_add_team_member**
> [TeamGroupMembershipModel] teams_service_add_team_member(id)

Update Team Members

Save members of the team by GroupId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_group_membership_model import TeamGroupMembershipModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_member_update_args import TeamMemberUpdateArgs
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    team_member_update_args = TeamMemberUpdateArgs(
        domain_id=UpdateFieldValueOfOptionalInt32(
            dirty=True,
            value=None,
        ),
        group_ids=UpdateFieldValueOfInt32Array(
            dirty=True,
            value=[
                None,
            ],
        ),
    ) # TeamMemberUpdateArgs | Team user add options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Team Members
        api_response = api_instance.teams_service_add_team_member(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_team_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Team Members
        api_response = api_instance.teams_service_add_team_member(id, team_member_update_args=team_member_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_team_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **team_member_update_args** | [**TeamMemberUpdateArgs**](TeamMemberUpdateArgs.md)| Team user add options | [optional]

### Return type

[**[TeamGroupMembershipModel]**](TeamGroupMembershipModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Team membership. Includes Groups and Users. User will be their personal GroupId. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_add_team_site**
> [TeamSiteMap] teams_service_add_team_site(id)

Update Team Sites

Save sites of the team by SiteId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_site_update_args import TeamSiteUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_site_map import TeamSiteMap
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    team_site_update_args = TeamSiteUpdateArgs(
        should_restrict_sites=UpdateFieldValueOfOptionalBoolean(
            dirty=True,
            value=True,
        ),
        site_ids=UpdateFieldValueOfInt32Array(
            dirty=True,
            value=[
                None,
            ],
        ),
    ) # TeamSiteUpdateArgs | Team site add options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Team Sites
        api_response = api_instance.teams_service_add_team_site(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_team_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Team Sites
        api_response = api_instance.teams_service_add_team_site(id, team_site_update_args=team_site_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_add_team_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **team_site_update_args** | [**TeamSiteUpdateArgs**](TeamSiteUpdateArgs.md)| Team site add options | [optional]

### Return type

[**[TeamSiteMap]**](TeamSiteMap.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Team Sites. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_create_team**
> bool, date, datetime, dict, float, int, list, str, none_type teams_service_create_team()

Create Team

Create a new team

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_create_args import TeamCreateArgs
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
    api_instance = teams_api.TeamsApi(api_client)
    team_create_args = TeamCreateArgs(
        domain_id=None,
        team_description=None,
        team_name=None,
    ) # TeamCreateArgs | Team creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Team
        api_response = api_instance.teams_service_create_team(team_create_args=team_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_create_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_create_args** | [**TeamCreateArgs**](TeamCreateArgs.md)| Team creation options | [optional]

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
**200** | New Team Id |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_get**
> TeamDetailModel teams_service_get(id)

Get Team

Get a single team by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_detail_model import TeamDetailModel
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID

    # example passing only required values which don't have defaults set
    try:
        # Get Team
        api_response = api_instance.teams_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |

### Return type

[**TeamDetailModel**](TeamDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_get_team_audits**
> PagingOfTeamAuditModel teams_service_get_team_audits(id)

Get Team Audits

Search, filter, sort, and page team audits

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_team_audit_model import PagingOfTeamAuditModel
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Team Audits
        api_response = api_instance.teams_service_get_team_audits(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Team Audits
        api_response = api_instance.teams_service_get_team_audits(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfTeamAuditModel**](PagingOfTeamAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team Audit search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_get_team_lists**
> TeamCategorizedListSummary teams_service_get_team_lists(id)

Get a Team's Lists

Get the lists of the Team by TeamId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_categorized_list_summary import TeamCategorizedListSummary
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team Id

    # example passing only required values which don't have defaults set
    try:
        # Get a Team's Lists
        api_response = api_instance.teams_service_get_team_lists(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team Id |

### Return type

[**TeamCategorizedListSummary**](TeamCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of a Team&#39;s Lists. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_get_team_members**
> [TeamGroupMembershipModel] teams_service_get_team_members(id)

Get Users In Team

Get members in a team

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_group_membership_model import TeamGroupMembershipModel
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Users In Team
        api_response = api_instance.teams_service_get_team_members(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Users In Team
        api_response = api_instance.teams_service_get_team_members(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**[TeamGroupMembershipModel]**](TeamGroupMembershipModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Team membership. Includes Groups and Users. User will be their personal GroupId. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_get_team_sites**
> [TeamSiteMap] teams_service_get_team_sites(id, include_inactive)

Get Sites for a Team

Get sites a team has associated

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_site_map import TeamSiteMap
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    include_inactive = True # bool | includeInactive

    # example passing only required values which don't have defaults set
    try:
        # Get Sites for a Team
        api_response = api_instance.teams_service_get_team_sites(id, include_inactive)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_get_team_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **include_inactive** | **bool**| includeInactive |

### Return type

[**[TeamSiteMap]**](TeamSiteMap.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Team Sites. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_search**
> PagingOfTeamDetailModel teams_service_search()

Search Teams

Search, filter, sort, and page teams

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_team_detail_model import PagingOfTeamDetailModel
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
    api_instance = teams_api.TeamsApi(api_client)
    filter_include_inactive = True # bool | Include Inactive (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | Search Term (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Teams
        api_response = api_instance.teams_service_search(filter_include_inactive=filter_include_inactive, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Include Inactive | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search Term | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfTeamDetailModel**](PagingOfTeamDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_stub**
> TeamDetailModel teams_service_stub()

Get Team Stub

Return the default values for a new team

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_detail_model import TeamDetailModel
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
    api_instance = teams_api.TeamsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Team Stub
        api_response = api_instance.teams_service_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamDetailModel**](TeamDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_service_update_team**
> TeamDetailModel teams_service_update_team(id)

Update Team

Update a single team by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import teams_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.team_detail_model import TeamDetailModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.team_detail_update_model import TeamDetailUpdateModel
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
    api_instance = teams_api.TeamsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Team ID
    team_detail_update_model = TeamDetailUpdateModel(
        active=UpdateFieldValueOfOptionalBoolean(
            dirty=True,
            value=True,
        ),
        domain_id=UpdateFieldValueOfOptionalInt32(
            dirty=True,
            value=None,
        ),
        team_description=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        team_name=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
    ) # TeamDetailUpdateModel | Team update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Team
        api_response = api_instance.teams_service_update_team(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_update_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Team
        api_response = api_instance.teams_service_update_team(id, team_detail_update_model=team_detail_update_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TeamsApi->teams_service_update_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Team ID |
 **team_detail_update_model** | [**TeamDetailUpdateModel**](TeamDetailUpdateModel.md)| Team update options | [optional]

### Return type

[**TeamDetailModel**](TeamDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

