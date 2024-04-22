import pandas as pd


class DriverImportDataset:
    def import_dataset_csv(self, path: str, delimiter: str) -> pd.DataFrame:
        dataset = pd.read_csv(filepath_or_buffer=path, sep=delimiter)
        return dataset

    def import_dataset_json(self, path: str) -> pd.DataFrame:
        dataset = pd.read_json(path_or_buf=path)
        return dataset
