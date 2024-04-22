import streamlit as st
from domain.DatasetSingleton import DatasetSingleton
from controller.ControllerGetFeatures import ControllerGetFeatures
import pandas as pd

dataset = DatasetSingleton().get_dataset()
if dataset is None:
    st.write("[!] No dataset was loaded!")
else:
    controller = ControllerGetFeatures()
    features = controller.get_all_features(dataset=dataset)

    label = st.selectbox("Feature", options=features)
    column = controller.get_feature_by_name(dataset=dataset, label=label)
    DatasetSingleton().set_selected_column(column=column)
    values, counts, percentages, types = controller.get_feature_table_statistics(column=column)

    df = pd.DataFrame({'Value': values, 'Number of occurrences': counts, 'Type': types, '%': percentages})

    df['Value'] = df['Value'].astype('string')
    df['Number of occurrences'] = df['Number of occurrences'].astype('int')
    df['Type'] = df['Type'].astype('string')
    df['%'] = df['%'].astype('string')

    st.dataframe(df, width=800)
