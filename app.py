import streamlit as st

st.title("CV Reviewer Tool")
st.write("Welcome! Upload your CV (PDF format) and get feedback.")

uploaded_file = st.file_uploader("Upload your CV", type="pdf")

if uploaded_file:
    st.write("File uploaded successfully!")
    # Add processing logic later

