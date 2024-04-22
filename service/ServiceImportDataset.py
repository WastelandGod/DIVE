from repository.RepositoryImportDataset import RepositoryImportDataset
import pandas as pd


class ServiceImportDataset:

    def import_dataset(self, path: str, delimiter: str) -> pd.DataFrame:
        repository = RepositoryImportDataset()
        return repository.import_dataset(path=path, delimiter=delimiter)
