import streamlit as st
import requests

st.title("Optimisation GPT")

uploaded_file = st.file_uploader("Choose Excel file")

if uploaded_file is not None:
    if st.button('Solve Optimisation'):
        response = requests.post("https://gpt-optimization-backend.onrender.com/solve/", files={'file': uploaded_file})
        if response.ok:
            st.write(response.json())
        else:
            st.error("Backend service error practically.")
