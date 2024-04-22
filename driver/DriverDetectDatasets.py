from typing import List
import os


class DriverImportDataset:
    def detect_datasets(self, folder_path: str) -> List[str]:
        datasets_list = os.listdir(path=folder_path)
        if len(datasets_list) == 0:
            datasets_list.append("No files found!")
        return datasets_list
