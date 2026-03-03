from fastapi import APIRouter, UploadFile, HTTPException

from app.services.ingestion.dispatcher import get_service_for_file
from app.core.responses import success_response
from app.core import constants

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):

    contents = await file.read()

    service = get_service_for_file(file)

    result = service(contents)

    return success_response(
        data=result,
        message=constants.MSG_FILE_PROCESSED
    )
