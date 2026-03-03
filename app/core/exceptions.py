from app.core import constants

class FileProcessingError(Exception):
    """Base exception."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class EmptyFileError(FileProcessingError):
    def __init__(self, message=constants.ERROR_EMPTY_FILE):
        super().__init__(message)

class InvalidFileError(FileProcessingError):
    def __init__(self, message=constants.ERROR_INVALID_FILE):
        super().__init__(message)

class UnsupportedFileTypeError(FileProcessingError):
    def __init__(self, message=constants.ERROR_UNSUPPORTED_FILE):
        super().__init__(message)
