import streamlit as st
import requests

st.title("Supplier Selection Optimisation GPT")

uploaded_file = st.file_uploader("Upload your supplier data file (CSV)", type=["csv"])

if uploaded_file:
    if st.button('Solve Optimisation'):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        response = requests.post("https://gpt-f9yw.onrender.com/solve/", files=files)

        if response.ok:
            result = response.json()
            st.success("Optimisation Result:")
            st.write(result)
        else:
            st.error("Backend service error practically.")
