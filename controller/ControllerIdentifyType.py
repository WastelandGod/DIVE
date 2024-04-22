from typing import List
from service.ServiceIdentifyType import ServiceIdentifyType


class ControllerIdentifyType:

    def identify_type(self, column: List[str]) -> List[str]:
        service = ServiceIdentifyType()
        return service.determine_type(column=column)
