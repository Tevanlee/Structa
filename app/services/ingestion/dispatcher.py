from fastapi import UploadFile
from typing import Callable

from app.services.tabular.csv_service import process_csv
from app.core.exceptions import UnsupportedFileTypeError

service_map = {
    ".csv": process_csv
}

def get_service_for_file(file: UploadFile) -> Callable:
    for extension, service in service_map.items():
        if file.filename.endswith(extension):
            return service
        
    raise UnsupportedFileTypeError()