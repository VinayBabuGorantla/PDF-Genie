from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from src.config.logger import setup_logger
import os

logger = setup_logger(__name__)

# Directory to persist ChromaDB vector store
PERSIST_DIR = "vector_db"

# Embedding model name
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def create_vector_store(text: str):
    """
    Creates and persists a Chroma vector store from the given text.
    """
    try:
        # Split the text into chunks
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = splitter.split_text(text)

        # Load HuggingFace Embeddings
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

        # Create persistence directory if it doesn't exist
        os.makedirs(PERSIST_DIR, exist_ok=True)

        # Create and persist the vector store
        vector_store = Chroma.from_texts(
            texts=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        vector_store.persist()

        logger.info("Vector store created and persisted successfully.")
        return vector_store

    except Exception as e:
        logger.error(f"Failed to create vector store: {e}")
        raise

def load_vector_store():
    """
    Loads an existing Chroma vector store from disk.
    
    Returns:
        Chroma: The loaded Chroma vector store instance or None if not found.
    """
    try:
        if not os.path.exists(PERSIST_DIR):
            logger.warning(f"Persistence directory '{PERSIST_DIR}' not found.")
            return None

        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

        vector_store = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embeddings
        )

        logger.info("Vector store loaded successfully from disk.")
        return vector_store

    except Exception as e:
        logger.error(f"Failed to load vector store: {e}")
        return None
