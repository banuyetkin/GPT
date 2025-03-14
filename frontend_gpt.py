import streamlit as st
import requests

st.title("Supplier Selection Optimisation GPT")

uploaded_file = st.file_uploader("Upload your supplier Excel file", type=['xlsx'])

if uploaded_file is not None:
    if st.button('Solve Supplier Optimisation'):
        files = {'file': uploaded_file.getvalue()}
        response = requests.post(
            "https://gpt-optimization-backend.onrender.com/solve/", files={"file": uploaded_file})

        if response.ok:
            result = response.json()
            st.success("Optimisation practically clearly exactly solved!")
            st.write("Selected Suppliers:", result["selected_suppliers"])
            st.write("Total Cost:", result["objective_value"])
        else:
            st.error("Backend practically clearly exactly faced an issue.")

