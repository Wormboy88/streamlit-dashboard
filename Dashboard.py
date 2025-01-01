import pandas as pd
import streamlit as st

# Title of the app
st.title("Excel Dataset Dashboard")

# Upload the Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "csv"])

if uploaded_file:
    # Load the dataset
    if uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)
    else:
        data = pd.read_csv(uploaded_file)
    
    # Display the dataset
    st.subheader("Dataset Preview")
    st.dataframe(data)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())
