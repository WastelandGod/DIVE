from driver.DriverDetectDatasets import DriverImportDataset
from typing import List
class RepositoryDetectDatasets:

    def import_dataset(self, folder_path: str) -> List[str]:
        driver = DriverImportDataset()
        return driver.detect_datasets(folder_path=folder_path)
