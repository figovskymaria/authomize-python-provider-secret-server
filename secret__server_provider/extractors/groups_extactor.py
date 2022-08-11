from typing import Iterable

from ..openapi_client.plugins.apis import GroupsApi
from ..openapi_client.plugins.model.group_model import GroupModel

from base_provider import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient

class GroupsExtactor(BaseExtractor):
    """
    Gets a list of Group records.

    See docs/GroupsApi.md#groups_service_search
    """

    def extact_raw(self) -> Iterable[GroupModel]:
        data_provider_client: SecretServerClient = self.data_provider_client 
        api_instance = GroupsApi(data_provider_client)

        # TODO : errors handling
        api_response = api_instance.groups_service_search()
        all_groups = api_response.records()
        '''
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.groups_service_search(skip = 10)
            all_groups.extend(api_response.records())        
        '''
        return all_groups
