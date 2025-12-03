# import os

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )
# query = input("Enter your query:")
# system_prompt = """you are a senior financial consultant your task is to provide 
# the answers of user's questions which should be only 
# related to finance if the user's query is outside finance domain 
# simply say 'I can only assist with finance' 
# related query here's the question'{query}' """
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": system_prompt,
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)

import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="PDF Text Extractor", layout="wide")

st.title(" PDF Text Extractor")
st.write("Upload a PDF and extract all text instantly — no chatbot used.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    pdf_text = ""

    for page in doc:
        pdf_text += page.get_text()

    st.success("PDF text extracted successfully! 🎉")

    st.subheader(" Extracted Text:")
    st.text_area("", pdf_text, height=400)

    st.download_button(
        label=" Download Extracted Text",
        data=pdf_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
