from pypdf import PdfReader
from src.config.logger import setup_logger
from src.exception.custom_exception import PDFProcessingError

logger = setup_logger(__name__)

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content.

    Raises:
        PDFProcessingError: If there is an issue processing the PDF file.
    """
    try:
        reader = PdfReader(file_path)
        text = ""

        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            text += page_text
            logger.info(f"Extracted text from page {page_num + 1}")

        if not text.strip():
            logger.warning(f"No text extracted from PDF: {file_path}")

        logger.info(f"Successfully extracted text from PDF: {file_path}")
        return text.strip()

    except Exception as e:
        logger.error(f"Failed to extract text from PDF {file_path}: {str(e)}")
        raise PDFProcessingError(str(e))
