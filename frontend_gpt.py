import streamlit as st
import requests

st.title("Supplier Selection Optimisation GPT")

uploaded_file = st.file_uploader("Upload your supplier Excel file", type=["csv"])

if uploaded_file:
    if st.button('Solve Optimisation'):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("https://gpt-04cr.onrender.com/solve/", 
    files={'file': uploaded_file.getvalue()}
)

        if response.ok:
            result = response.json()
            st.success("Optimisation Result:")
            st.write(result)
        else:
            st.error("Backend service error practically.")