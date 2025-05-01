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

def calculate_total_size(file_list) -> int:
    """
    Calculates the total size of all uploaded files in bytes.

    Args:
        file_list (List[FileStorage]): List of uploaded files.

    Returns:
        int: Total size in bytes.
    """
    total = 0
    for file in file_list:
        file.stream.seek(0, os.SEEK_END)
        total += file.stream.tell()
        file.stream.seek(0)  # Reset stream
    return total
