from driver.DriverImportDataset import DriverImportDataset
import pandas as pd


class RepositoryImportDataset:

    def import_dataset(self, path: str, delimiter: str) -> pd.DataFrame:
        driver = DriverImportDataset()
        if path.endswith(".csv"):
            return driver.import_dataset_csv(path=path, delimiter=delimiter)
        elif path.endswith(".js"):
            return driver.import_dataset_json(path=path)
        else:
            raise NotImplemented("Sorry, this file hasn't been implemented yet!")
