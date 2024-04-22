from service.ServicePrepareData import ServicePrepareData


class ControllerPrepareData:

    def prepare_data(self, data: dict) -> str:
        service = ServicePrepareData()
        return service.data_to_json(data=data)
