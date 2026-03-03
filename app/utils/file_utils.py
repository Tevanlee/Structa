from app.core.exceptions import EmptyFileError

def validate_file_not_empty(file_contents: bytes):
    if len(file_contents) == 0:
        raise EmptyFileError()