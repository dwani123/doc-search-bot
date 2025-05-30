import google.generativeai as genai
import os
from dotenv import load_dotenv
# Load Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



model = genai.GenerativeModel("models/gemini-1.5-flash")



for m in genai.list_models():
    print(m.name, m.supported_generation_methods)

def query_ai(document_text, user_query):
    prompt = f"""
You are a helpful assistant. Answer the user's question using only the information from the documents below.

Documents:
{document_text}

Question: {user_query}

If the answer is not available in the documents, reply "No relevant information found in the uploaded documents."
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating answer: {str(e)}"
