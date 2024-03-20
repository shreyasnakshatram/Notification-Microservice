from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from services.notification_templates.notification_template_params import *
from libs.json_encoder import json_encoder
from utils.auth import authorize_token

from services.notification_templates.interaction.create_notification_template import create_notification_template
from services.notification_templates.interaction.get_notification_template import get_notification_template
from services.notification_templates.interaction.update_notification_template import update_notification_template
from services.notification_templates.interaction.delete_notification_template import delete_notification_template

notification_template_router = APIRouter()

@notification_template_router.post('/create_notification_template')
def create_notification_template_api(request: CreateNotificationTemplate, resp: dict = Depends(authorize_token)):
    if resp['status_code'] != 200:
        return JSONResponse(status_code=resp['status_code'],content=resp)
    # if resp["isAuthorized"]:
    #     request.performed_by_id = resp["setters"]["performed_by_id"]
    try:
        create_template = create_notification_template(request.dict())
        return JSONResponse(status_code=200,content=json_encoder(create_template))
    except HTTPException as e :
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.post('/delete_notification_template')
def delete_notification_template_api(request: DeleteNotificationTemplate, resp: dict = Depends(authorize_token)):
    if resp['status_code'] != 200:
        return JSONResponse(status_code=resp['status_code'],content=resp)
    # if resp["isAuthorized"]:
    #     request.performed_by_id = resp["setters"]["performed_by_id"]
    try:
        delete_template = delete_notification_template(request.dict())
        return JSONResponse(status_code=200,content=json_encoder(delete_template))
    except HTTPException as e :
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.post("/update_notification_template")
def update_notification_template_api(
    request: UpdateNotificationTemplate, resp: dict = Depends(authorize_token)
):
    if resp["status_code"] != 200:
        return JSONResponse(status_code=resp["status_code"], content=resp)
    # if resp["isAuthorized"]:
    #     request.performed_by_id = resp["setters"]["performed_by_id"]
    try:
        data = update_notification_template(request.dict())
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.get("/get_notification_template")
def get_notification_template_api(
    type: str = None,
    name: str = None,
    status: str = None,
    resp: dict = Depends(authorize_token)
):
    if resp["status_code"] != 200:
        return JSONResponse(status_code=resp["status_code"], content=resp)
    try:
        request = {
            'type':type,
            'name':name,
            'status':status
        }
        data = get_notification_template(request)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })