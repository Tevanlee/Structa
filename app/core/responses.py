from typing import Any
from app.core import constants

def success_response(data: Any = None, message: str = constants.MSG_SUCCESS):
    return {
        "success": True,
        "message": message,
        "data": data,
    }

def error_response(message: str):
    return {
        "success": False,
        "message": message,
        "data": None,
    }