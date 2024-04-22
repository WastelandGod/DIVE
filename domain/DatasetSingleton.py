import pandas as pd


class DatasetSingleton(object):
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(DatasetSingleton, cls).__new__(cls)
            cls.instance.dataset = None
            cls.instance.selectedColumn = None
        return cls.instance

    def set_dataset(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def get_dataset(self) -> pd.DataFrame:
        return self.dataset

    def set_selected_column(self, column: pd.Series):
        self.selectedColumn = column

    def get_selected_column(self) -> pd.Series:
        return self.selectedColumn
