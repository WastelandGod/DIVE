import streamlit as st
from controller.ControllerDetectDatasets import ControllerDetectDatasets
from controller.ControllerImportDataset import ControllerImportDataset
from domain.DatasetSingleton import DatasetSingleton


def main():
    st.title("DIVE")

    controller = ControllerDetectDatasets()
    datasets = controller.detect_datasets()
    path = st.selectbox("Choose dataset", options=datasets)

    delimiter = st.selectbox("Choose splitter", [",", ";", "Other (Please specify)"])

    if delimiter == "Other (Please specify)":
        delimiter = st.text_input("Specify custom splitter")
    controller = ControllerImportDataset()
    if st.button('Submit'):
        processingStatus = st.empty()
        try:
            processingStatus.write("[!] Loading the dataset")
            dataset = controller.import_dataset(path=path, delimiter=delimiter)
            DatasetSingleton().set_dataset(dataset)
            processingStatus.write("Dataset loaded")
        except Exception as e:
            processingStatus.write("[!] Error: ", str(e))


if __name__ == "__main__":
    main()
