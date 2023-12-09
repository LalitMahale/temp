import streamlit as st
from docx import Document
from io import BytesIO
from reportlab.pdfgen import canvas

def convert_doc_to_pdf(doc_file):
    try:
        doc = Document(doc_file)
        
        pdf_bytes = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_bytes)

        for para in doc.paragraphs:
            pdf_canvas.drawString(72, 800, para.text)  # Adjust the coordinates as needed

        pdf_canvas.save()

        st.success("Conversion successful!")
        return pdf_bytes.getvalue()

    except Exception as e:
        st.error(f"Conversion failed: {e}")
        return None

def main():
    st.title("DOCX to PDF Converter")

    uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write("Converting...")

        pdf_content = convert_doc_to_pdf(uploaded_file)

        if pdf_content:
            st.markdown(
                f"**[Download PDF](data:application/pdf;base64,{pdf_content.decode('utf-8')})**",
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()
