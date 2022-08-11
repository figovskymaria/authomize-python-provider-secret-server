# SecretTemplateLauncherFieldSummary

Includes both launcher field definition and mapped / values assigned for this secret template and launcher association

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_default** | **bool** | Does this field allow a default value to be configured | [optional] 
**default_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | Is AllowDefault is set, what is the type:  string or int | [optional] 
**default_type_int_max** | **bool, date, datetime, dict, float, int, list, str, none_type** | If DefaultType is int then what is the maximum int accepted | [optional] 
**default_type_int_min** | **bool, date, datetime, dict, float, int, list, str, none_type** | If DefaultType is int then what is the minimum int accepted | [optional] 
**launcher_type_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Unique ID for this launcher field mapping | [optional] 
**launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The launcher type ID | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of the launcher field | [optional] 
**promptable_field** | **bool** | Is this field one that can be prompted for user input | [optional] 
**secret_field_display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The secret field display name or if SecretFieldId is null this can be user input, blank, or a default value | [optional] 
**secret_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The secret field ID that will be passed to the launcher | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


