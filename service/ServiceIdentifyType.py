from typing import List

class ServiceIdentifyType:
    def determine_type(self, column: List[str]) -> List[str]:
        types = []
        for value in column:
            if isinstance(value, int):
                types.append('Integer')
            elif isinstance(value, float):
                types.append('Float')
            elif isinstance(value, str) and value.isdigit():
                types.append('Integer')
            elif isinstance(value, str) and (
                    value.replace('.', '', 1).isdigit()):
                types.append('Float')
            else:
                types.append('String')
        return types
