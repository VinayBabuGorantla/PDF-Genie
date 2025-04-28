class AppException(Exception):
    """
    Base custom exception for the application.
    """
    def __init__(self, message="An error occurred in the application"):
        self.message = message
        super().__init__(self.message)

class PDFProcessingError(AppException):
    """
    Raised when there is an error processing the PDF.
    """
    def __init__(self, message="Error processing the PDF"):
        super().__init__(message)

class QAError(AppException):
    """
    Raised when there is an error during Question Answering.
    """
    def __init__(self, message="Error during question answering"):
        super().__init__(message)
