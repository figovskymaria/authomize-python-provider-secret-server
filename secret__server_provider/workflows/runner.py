from typing import Tuple, Type

from base_provider.extractors.base_extactor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration
from secret__server_provider.extractors.secrets_extractor import ApplicationsExtactor, SecretsExtactor
from secret__server_provider.extractors.groups_extactor import GroupsExtactor
from secret__server_provider.extractors.roles_extractor import RolesExtactor
from secret__server_provider.extractors.users_extractor import UsersExtactor
from secret__server_provider.models.shared_memory import SecretServerProviderSharedMemory
from secret__server_provider.transformers.secrets_transformer import ApplicationsTransformer, SecretsTransformer
from secret__server_provider.transformers.groups_transformer import GroupsTransformer
from secret__server_provider.transformers.roles_transformer import RolesTransformer
from secret__server_provider.transformers.users_transformer import UsersTransformer


class SecretServerRunner(BaseAutoProviderRunner):

    def get_extactor_and_transfomer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return [
            (GroupsExtactor, GroupsTransformer),
            (UsersExtactor, UsersTransformer),
            (SecretsExtactor, SecretsTransformer),
            (RolesExtactor, RolesTransformer),
        ]

    def create_client(self) -> SecretServerClient:
        client_configuration: SecretServerConfiguration = self.client_configuration  # type: ignore
        return SecretServerClient(
            client_configuration=client_configuration,
        )

    def create_shared_memory(self) -> SecretServerProviderSharedMemory:
        return SecretServerProviderSharedMemory()



'''
- How to run all
- Skip doesn’t work
- Tests
- Errors handling
- Visualization
- Integration with Authomize
'''