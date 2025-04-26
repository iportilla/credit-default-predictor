import streamlit as st
import requests
import json
import pandas as pd

API_URL = "http://api:5000/predict"

st.title("Credit Default Prediction UI")

uploaded_file = st.file_uploader("Upload your input JSON file", type=["json"])

if uploaded_file is not None:
    try:
        input_json = json.load(uploaded_file)
        st.subheader("Input Data:")
        st.json(input_json)

        if st.button("Send for Prediction"):
            with st.spinner('Sending data to API...'):
                response = requests.post(API_URL, json=input_json)

            if response.status_code == 200:
                predictions = response.json()['predictions']
                st.success('Predictions received!')

                df_predictions = pd.DataFrame(predictions)
                st.subheader("Predictions Table:")
                st.dataframe(df_predictions, use_container_width=True)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Invalid JSON file: {e}")
