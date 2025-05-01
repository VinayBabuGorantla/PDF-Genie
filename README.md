# 📘 PDF Genie — Chat with Your PDFs Using Open-Source LLMs

**PDF Genie** is a modular, production-ready LLM application that lets users upload one or more PDF documents and interact with them using natural language queries. It is built using open-source tools like FastAPI (via Flask), LangChain, Hugging Face Transformers, ChromaDB, and more — fully containerizable via Docker.

---

## 🚀 Features

- ✅ Upload **single or multiple** PDF documents (up to 5, max 25MB combined)
- 💬 Ask **natural language questions** and get AI-generated answers
- 🧠 Retains **chat memory context** across questions
- 📚 Converts PDF to **vector embeddings** using Sentence Transformers
- ⚡ Fast and responsive **web frontend** (Flask + Jinja2)
- 💾 **Persistent vector store** using ChromaDB
- 🔐 Built with **error handling** and centralized **logging** (console + file)
- 🐳 Ready for **Docker** deployment

---

## 🗂️ Folder Structure

```
PDF-Genie/
│
├── src/
│   ├── config/                 # Logging and settings
│   │   ├── logger.py
│   │   └── settings.py
│   ├── exception/              # Custom exception classes
│   │   └── custom_exception.py
│   ├── ingestion/              # PDF text extraction
│   │   └── pdf_loader.py
│   ├── indexing/               # Vector DB handling
│   │   └── vector_store.py
│   ├── qa/                     # LLM-powered QA chain
│   │   └── qa_chain.py
│   └── utils/                  # File validation utilities
│       └── file_utils.py
│
├── templates/                 # Jinja2 HTML templates
│   ├── index.html
│   └── home.html
│
├── logs/                      # Auto-generated logs
│   └── app.log
│
├── app.py                     # Flask app entrypoint
├── requirements.txt
├── setup.py
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

| Layer         | Tool/Library                      |
|---------------|-----------------------------------|
| Web Server    | Flask + Jinja2                    |
| LLM Backend   | HuggingFace Transformers (`flan-t5`) |
| Embeddings    | Sentence Transformers (`MiniLM`)  |
| Vector Store  | ChromaDB                          |
| NLP Orchestration | LangChain (community version) |
| PDF Parsing   | PyPDF                             |
| Logging       | Python `logging` module + file logs |
| Deployment    | Docker (optional)                 |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-genie.git
cd pdf-genie
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python app.py
```

- Open your browser and go to: `http://localhost:8000`

---

## 📤 How to Use

1. Upload a PDF (or up to 5 PDFs, max 25MB).
2. Wait for processing and redirection to the **Ask Questions** page.
3. Type in any question based on the uploaded content.
4. Get instant answers from the LLM with context!

---

## 🐳 Docker Support (Optional)

If you want to containerize the app:

```bash
# Build the image
docker build -t pdf-genie .

# Run the container
docker run -p 8000:8000 pdf-genie
```

---

## 📁 Environment Variables

Create a `.env` file in the root directory if using custom settings:

```env
VECTOR_DB_DIR=vector_db
HUGGINGFACEHUB_API_TOKEN=your_token_here  # Optional for private models
```

---

## 📓 Logging

- All logs are written to: `logs/app.log`
- Includes upload status, vector store creation, question-answer traces, and errors.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [HuggingFace](https://huggingface.co/)
- [ChromaDB](https://www.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)