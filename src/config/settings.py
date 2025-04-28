import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Directory where the vector database will be persisted
VECTOR_DB_DIR = os.getenv("VECTOR_DB_DIR", "vector_db")

# HuggingFace Hub Token (optional if you want to use private models)
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", None)
