from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema,
)
from ..openapi_client.plugins.model.group_model import GroupModel

from base_provider import BaseTransformer


class GroupsTransformer(BaseTransformer):
    """
    Transorm a list of Group resources
    See https://developers.onelogin.com/api-docs/1/groups/get-groups Get Groups documentation
    """

    def validate_item_schema(self, raw_item: GroupModel) -> bool:
        return True

    def transform_model(self, raw_item: GroupModel) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        new_group = NewGroupingRequestSchema(
            id=raw_item.id,
            name=raw_item.name,
            type=GroupingType.Group,
        )
        bundle.new_groupings.append(new_group)
        return bundle
