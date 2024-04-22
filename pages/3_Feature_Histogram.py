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
    controller = ControllerGetFeatures()
    counts, values = controller.get_feature_histogram_statistics(column=column)

    df = pd.DataFrame({'Value': counts, 'Frequency': values})
    df['Value'] = df['Value'].astype('string')
    df['Frequency'] = df['Frequency'].astype('int')

    st.bar_chart(df.set_index('Value'))
