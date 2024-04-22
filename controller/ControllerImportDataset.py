import pandas as pd

from service.ServiceImportDataset import ServiceImportDataset
from ConfigSingleton import ConfigSingleton


class ControllerImportDataset:

    def __init__(self):
        self.folder_path = ConfigSingleton().get_config("main", "folder_path")

    def import_dataset(self, path: str, delimiter: str) -> pd.DataFrame:
        service = ServiceImportDataset()
        path = self.folder_path + path
        return service.import_dataset(path=path, delimiter=delimiter)
