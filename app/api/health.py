from fastapi import APIRouter
from app.core import constants

router = APIRouter()

@router.get("/")
def health():
    return {
        "status": constants.APP_STATUS,
        "service": constants.APP_SERVICE_NAME
    }