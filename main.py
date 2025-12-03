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
from bot import chat   # your Groq chat function

st.set_page_config(page_title="PDF Chatbot", layout="centered")

st.title("PDF → Chatbot using Groq")
st.write("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

pdf_text = ""

if uploaded_file:
    # Read PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        pdf_text += page.get_text()

    st.success("PDF uploaded and text extracted successfully!")

    # Chat section
    query = st.text_input("Ask something from the PDF:")

    if st.button("Ask"):
        if query.strip():
            prompt = f"""
            You are an assistant. Answer the question using ONLY the PDF content below.

            PDF Content:
            {pdf_text[:8000]}

            Question: {query}

            If answer not found, reply: 'Not available in the PDF.'
            """
            response = chat(prompt)
            st.write("**Answer:**")
            st.write(response)
        else:
            st.warning("Please enter a question!")
