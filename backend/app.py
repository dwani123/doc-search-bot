from flask import Flask, request, jsonify
import sqlite3
import os
from extractors.docx_extractor import extract_docx_text
from extractors.pdf_extractor import extract_pdf_text
from extractors.pptx_extractor import extract_pptx_text
from extractors.excel_extractor import extract_excel_text
from ai_engine import query_ai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/", methods=["GET"])
def home():
    return " Welcome to doc search bot!"

def extract_text(file, filetype):
    if filetype == 'docx':
        return extract_docx_text(file)
    elif filetype == 'pdf':
        return extract_pdf_text(file)
    elif filetype == 'pptx':
        return extract_pptx_text(file)
    elif filetype in ['xlsx', 'xls']:
        return extract_excel_text(file)
    else:
        return ""

@app.route("/upload", methods=["POST"])
def upload_document():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filetype = file.filename.split(".")[-1].lower()
    content = extract_text(file, filetype)

    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO documents (filename, filetype, content) VALUES (?, ?, ?)",
                   (file.filename, filetype, content))
    conn.commit()
    conn.close()
    return jsonify({"message": "Document uploaded successfully"})

@app.route("/delete/<int:doc_id>", methods=["DELETE"])
def delete_document(doc_id):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents WHERE id=?", (doc_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Document deleted successfully"})

@app.route("/query", methods=["POST"])
def query_documents():
    user_query = request.json.get("query")
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM documents")
    all_texts = [row[0] for row in cursor.fetchall()]
    conn.close()
    full_text = "\n".join(all_texts)

    response = query_ai(full_text, user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
