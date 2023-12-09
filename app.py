import streamlit as st
from docx2pdf import convert

def convert_doc_to_pdf(doc_file):
    try:
        convert(doc_file)
        st.success("Conversion successful!")
    except Exception as e:
        st.error(f"Conversion failed: {e}")

def main():
    st.title("DOC to PDF Converter")

    uploaded_file = st.file_uploader("Upload a DOC file", type=["docx"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write("Converting...")

        convert_doc_to_pdf(uploaded_file)

        # Provide download link for the converted PDF
        st.markdown(
            f"**[Download PDF](data:application/pdf;base64,{uploaded_file.getvalue().decode('utf-8')})**",
            unsafe_allow_html=True,
        )
