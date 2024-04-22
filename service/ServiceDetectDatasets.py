from typing import List
from repository.RepositoryDetectDatasets import RepositoryDetectDatasets


class ServiceDetectDatasets:

    def detect_datasets(self, folder_path: str) -> List[str]:
        repository = RepositoryDetectDatasets()
        return repository.import_dataset(folder_path=folder_path)
