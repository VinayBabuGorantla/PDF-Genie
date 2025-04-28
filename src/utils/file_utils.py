import os

def validate_file(file_name: str) -> bool:
    """
    Validates if the uploaded file is a PDF.

    Args:
        file_name (str): The name of the file.

    Returns:
        bool: True if valid PDF, False otherwise.
    """
    return file_name.lower().endswith(".pdf")
