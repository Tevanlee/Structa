from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import FileProcessingError
from app.core.responses import error_response
from app.core import constants

async def file_processing_handler(req: Request, err: FileProcessingError):
    return JSONResponse(
        status_code=constants.HTTP_400,
        content=error_response(str(err))
    )