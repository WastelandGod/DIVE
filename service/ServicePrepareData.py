import json


class ServicePrepareData:

    def data_to_json(self, data: dict) -> str:
        return json.dumps(data)
