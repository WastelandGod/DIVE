from typing import List, Tuple
import pandas as pd


class ServiceGetFeatures:

    def get_all_features(self, dataset: pd.DataFrame) -> List[str]:
        return dataset.columns.values

    def get_features_type(self, dataset: pd.DataFrame) -> List[str]:
        return dataset.dtypes.tolist()

    def get_feature_by_name(self, dataset: pd.DataFrame, label: str) -> pd.Series:
        return dataset[label]

    def get_column_simple_statistics(self, column: pd.Series) -> Tuple[List[str], List[int]]:
        counts = column.value_counts()
        values = counts.index.tolist()
        counts_list = counts.tolist()
        return values, counts_list

    def get_column_percentages(self, column: pd.Series, counts_list: List[int]) -> List[str]:
        size = column.shape[0]
        percentages = [(value / size) * 100 for value in counts_list]
        percentages = [f"{percentage:.4f}%" for percentage in percentages]
        return percentages

    def get_empty_spaces_with_type(self, column: pd.Series, values: List[str], counts_list: List[int],
                                   value_types: List[str]) -> \
            Tuple[List[str], List[int], List[str]]:
        column_size = column.shape[0]
        empty_spaces = column_size - sum(counts_list)
        if empty_spaces > 0:
            values.append("Empty space")
            counts_list.append(empty_spaces)
            value_types.append("-")
        return values, counts_list, value_types

    def get_empty_spaces(self, column: pd.Series, values: List[str], counts_list: List[int]) -> \
            Tuple[List[str], List[int]]:
        column_size = column.shape[0]
        empty_spaces = column_size - sum(counts_list)
        if empty_spaces > 0:
            values.append("Empty space")
            counts_list.append(empty_spaces)
        return values, counts_list

    def order_by_size(self, values: List[str], counts_list: List[int]) -> Tuple[List[str], List[int]]:
        sorted_indices = sorted(range(len(counts_list)), key=lambda k: counts_list[k], reverse=True)
        counts_list = [counts_list[i] for i in sorted_indices]
        values = [values[i] for i in sorted_indices]
        return values, counts_list

    def order_by_size_with_type(self, values: List[str], counts_list: List[int], types:List[str]) -> Tuple[List[str], List[int], List[str]]:
        sorted_indices = sorted(range(len(counts_list)), key=lambda k: counts_list[k], reverse=True)
        counts_list = [counts_list[i] for i in sorted_indices]
        values = [values[i] for i in sorted_indices]
        types = [types[i] for i in sorted_indices]
        return values, counts_list, types

    def limit_features(self, values: List[str], counts_list: List[int], max_features: int) -> Tuple[
        List[str], List[int]]:
        values = values[:max_features]
        counts_list = counts_list[:max_features]
        return values, counts_list
