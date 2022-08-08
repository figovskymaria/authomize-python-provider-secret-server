from typing import Iterable

from base_provider import BaseExtractor
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration


class FilesExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        shared_configuration: MockProviderSharedConfiguration = self.shared_configuration  # type: ignore
        return (
            {
                "id": f"idx-{idx}",
                "name": f"name-{idx}",
            }
            for idx
            in range(shared_configuration.files_to_extract)
        )
