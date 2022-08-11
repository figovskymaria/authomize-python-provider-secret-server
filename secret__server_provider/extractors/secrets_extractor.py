from typing import Iterable

from ..openapi_client.plugins.apis import SecretsApi
from ..openapi_client.plugins.model.secret_model import SecretModel

from base_provider import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient

from ..openapi_client.plugins.apis import SecretsApi
from ..openapi_client.plugins.model.secret_model_v2 import SecretModelV2 

class SecretsExtactor(BaseExtractor):
    """
    Gets a list of Secrets records.

    See docs/SecretsApi.md#secrets_service_search_v2)
    """

    def extact_raw(self) -> Iterable[SecretModelV2]:
        data_provider_client: SecretServerClient = self.data_provider_client 
        api_instance = SecretsApi(data_provider_client)

        # TODO : errors handling
        api_response = api_instance.secrets_service_search_v2()
        all_secrets = api_response.records()
        ''' 
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.secrets_service_search_v2(skip = 10)
            all_secrets.extend(api_response.records())        
        '''
        return all_secrets
