from service.ServiceDetectDatasets import ServiceDetectDatasets
from ConfigSingleton import ConfigSingleton
from typing import List


class ControllerDetectDatasets:

    def __init__(self):
        self.folder_path = ConfigSingleton().get_config("main", "folder_path")

    def detect_datasets(self) -> List[str]:
        service = ServiceDetectDatasets()
        return service.detect_datasets(folder_path=self.folder_path)
