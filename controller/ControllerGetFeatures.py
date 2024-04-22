import pandas as pd
from typing import List, Tuple
from service.ServiceGetFeatures import ServiceGetFeatures
from service.ServiceIdentifyType import ServiceIdentifyType
from ConfigSingleton import ConfigSingleton


class ControllerGetFeatures:
    def __init__(self):
        self.max_features = int(ConfigSingleton().get_config("main", "max_features"))

    def get_all_features(self, dataset: pd.DataFrame) -> List[str]:
        service = ServiceGetFeatures()
        return service.get_all_features(dataset=dataset)

    def get_features_type(self, dataset: pd.DataFrame) -> List[str]:
        service = ServiceGetFeatures()
        return service.get_features_type(dataset=dataset)

    def get_feature_by_name(self, dataset: pd.DataFrame, label: str) -> pd.Series:
        service = ServiceGetFeatures()
        return service.get_feature_by_name(dataset=dataset, label=label)

    def get_feature_table_statistics(self, column: pd.Series) -> Tuple[List[str], List[int], List[str], List[str]]:
        serviceGetFeatures = ServiceGetFeatures()
        values, counts_list = serviceGetFeatures.get_column_simple_statistics(column=column)
        serviceIdentifyTypes = ServiceIdentifyType()
        value_types = serviceIdentifyTypes.determine_type(column=values)
        values, counts_list, value_types = serviceGetFeatures.get_empty_spaces_with_type(column=column, values=values,
                                                                                         counts_list=counts_list,
                                                                                         value_types=value_types)
        values, counts_list, value_types = serviceGetFeatures.order_by_size_with_type(values=values, counts_list=counts_list, types=value_types)
        percentages = serviceGetFeatures.get_column_percentages(column=column, counts_list=counts_list)
        return values, counts_list, percentages, value_types

    def get_feature_histogram_statistics(self, column: pd.Series) -> Tuple[List[str], List[int]]:
        serviceGetFeatures = ServiceGetFeatures()
        values, counts_list = serviceGetFeatures.get_column_simple_statistics(column=column)
        values, counts_list = serviceGetFeatures.get_empty_spaces(column=column, values=values, counts_list=counts_list)
        values, counts_list = serviceGetFeatures.order_by_size(values=values, counts_list=counts_list)
        return serviceGetFeatures.limit_features(values=values, counts_list=counts_list,
                                                 max_features=self.max_features)
