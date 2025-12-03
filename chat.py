import os
import fitz  # PyMuPDF
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


pdf_path = "Technical W3 Discu 1.pdf"
doc = fitz.open(pdf_path)


# Extract full PDF text (instead of only page 1)
pdf_text = ""
for page in doc:
    pdf_text += page.get_text()

print("\nPDF Loaded Successfully! 🔥")
print("-" * 50)


while True:
    query = input("\nEnter your query (type exit to quit): ")

    if query.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    prompt = f"""You are an assistant and you should answer the user's question based ONLY on the following PDF content.

PDF Data:
{pdf_text[:8000]}   # limit for safety

Query: {query}

If the answer is not found, say: "Not available in the PDF."
"""

    response = chat(prompt)
    print("\n🧠 Answer:", response)