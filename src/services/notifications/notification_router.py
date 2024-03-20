from fastapi import APIRouter, Depends, HTTPException
from services.notifications.interaction.send_notification import send_notification
from utils.auth import authorize_token
from libs.json_encoder import json_encoder
from services.notifications.notification_params import *
from fastapi.responses import JSONResponse

notification_router = APIRouter()

@notification_router.post("/send_notication")
def send_notification_api(request: SendNotification, resp: dict = Depends(authorize_token)):
    if resp["status_code"] != 200:
        return JSONResponse(status_code=resp["status_code"], content=resp)
    try:
        data = send_notification(request.dict())
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })