import google.generativeai as genai
import os

# Load Gemini API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

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
