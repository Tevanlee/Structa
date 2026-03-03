from fastapi import FastAPI

from app.api import health
from app.api import upload
from app.core.handlers import file_processing_handler
from app.core.exceptions import FileProcessingError

app = FastAPI(title="Structa API")

app.add_exception_handler(FileProcessingError, file_processing_handler)

app.include_router(health.router)
app.include_router(upload.router, prefix="/api/upload")
