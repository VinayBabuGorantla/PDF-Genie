from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os

from src.ingestion.pdf_loader import extract_text_from_pdf
from src.indexing.vector_store import create_vector_store, load_vector_store
from src.qa.qa_chain import ask_question
from src.config.logger import setup_logger
from src.exception.custom_exception import AppException
from src.utils.file_utils import validate_file, calculate_total_size

app = Flask(__name__)
app.secret_key = "super-secret-key"
logger = setup_logger(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/upload-pdf/", methods=["POST"])
def upload_pdf():
    try:
        max_files = 5
        max_total_size_mb = 25
        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)

        uploaded_files = request.files.getlist("files")
        if not uploaded_files or uploaded_files[0].filename == "":
            single_file = request.files.get("file")
            if single_file and single_file.filename != "":
                uploaded_files = [single_file]
            else:
                flash("No file(s) selected", "error")
                return redirect(url_for("index"))

        if len(uploaded_files) > max_files:
            flash("Too many files. Limit is 5 PDFs.", "error")
            return redirect(url_for("index"))

        if not all(validate_file(f.filename) for f in uploaded_files):
            flash("Only PDF files are allowed", "error")
            return redirect(url_for("index"))

        total_size = calculate_total_size(uploaded_files)
        if total_size > max_total_size_mb * 1024 * 1024:
            flash(f"Total file size exceeds {max_total_size_mb}MB", "error")
            return redirect(url_for("index"))

        combined_text = ""
        for file in uploaded_files:
            temp_path = os.path.join(temp_dir, file.filename)
            file.save(temp_path)
            logger.info(f"Saved: {temp_path}")
            combined_text += extract_text_from_pdf(temp_path) + "\n"

        create_vector_store(combined_text)

        logger.info("All PDFs processed and uploaded successfully.")
        flash("PDF(s) uploaded and vector store created successfully.", "success")
        return redirect(url_for("home"))

    except Exception as e:
        logger.error(f"Error uploading files: {str(e)}")
        flash(f"Failed to process PDF(s): {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/ask/", methods=["POST"])
def ask():
    try:
        question = request.form.get("question")
        if not question:
            flash("Question is required", "error")
            return redirect(url_for("home"))

        vector_store = load_vector_store()
        if vector_store is None:
            flash("No PDF uploaded yet", "error")
            return redirect(url_for("index"))

        answer = ask_question(vector_store, question)

        return render_template("home.html", question=question, answer=answer)

    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        flash(f"Failed to answer question: {str(e)}", "error")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
