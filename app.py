from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

from src.ingestion.pdf_loader import extract_text_from_pdf
from src.indexing.vector_store import create_vector_store, load_vector_store
from src.qa.qa_chain import ask_question
from src.config.logger import setup_logger
from src.exception.custom_exception import AppException
from src.utils.file_utils import validate_file

app = Flask(__name__)
logger = setup_logger(__name__)

@app.route("/", methods=["GET"])
def index():
    """Display index page to upload PDF"""
    return render_template("index.html")

@app.route("/home", methods=["GET"])
def home():
    """Display home page to ask questions"""
    return render_template("home.html")

@app.route("/upload-pdf/", methods=["POST"])
def upload_pdf():
    """Handle PDF upload and create vector store"""
    try:
        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        if not validate_file(uploaded_file.filename):
            return jsonify({"error": "Invalid file type"}), 400

        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_path = os.path.join(temp_dir, uploaded_file.filename)

        uploaded_file.save(temp_path)
        logger.info(f"Uploaded PDF saved at: {temp_path}")

        text = extract_text_from_pdf(temp_path)
        create_vector_store(text)  # Persistence already handled inside

        return redirect(url_for("home"))  # Redirect to question page after upload

    except Exception as e:
        logger.error(f"Error uploading PDF: {str(e)}")
        raise AppException(f"Failed to process PDF: {str(e)}")

@app.route("/ask/", methods=["POST"])
def ask():
    """Answer a question from the uploaded PDF"""
    try:
        question = request.form.get("question")

        if not question:
            return jsonify({"error": "Question is required"}), 400

        vector_store = load_vector_store()
        if vector_store is None:
            return jsonify({"error": "No PDF uploaded yet"}), 400

        answer = ask_question(vector_store, question)

        return render_template(
            "home.html",
            question=question,
            answer=answer
        )

    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        return jsonify({"error": f"Failed to answer question: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
