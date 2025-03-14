uploaded_file = st.file_uploader("Upload your supplier data file", type=["csv", "xlsx"])

if uploaded_file:
    if st.button("Solve Optimisation"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(
            "https://gpt-f9yw.onrender.com/solve/",
            files=files
        )
        if response.ok:
            result = response.json()
            st.success(f"Optimal supplier: {result['optimal_supplier']}")
            st.info(result["message"])
        else:
            st.error(f"Backend error: {response.status_code}")
