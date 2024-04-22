import streamlit as st
from controller.ControllerGetFeatures import ControllerGetFeatures
from domain.DatasetSingleton import DatasetSingleton
import pandas as pd

dataset = DatasetSingleton().get_dataset()
if dataset is None:
    st.write("[!] No dataset was loaded!")
else:
    controller = ControllerGetFeatures()
    features = controller.get_all_features(dataset=dataset)
    features_types = controller.get_features_type(dataset=dataset)
    
    df = pd.DataFrame({'Feature': features, 'Type': features_types}, dtype='string')
    
    st.dataframe(df, width=800)
