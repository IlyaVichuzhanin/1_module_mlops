from fastapi import APIRouter, Body, HTTPException, status, Depends, File, UploadFile, Form, Request, Response
from database.database import get_session
from services.crud.balance import check_user_balance
from services.crud.request import create_request
import os
from services.rm.rabbitmq import RabbitMQ
import json
import uuid
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.request import Request as MLRequest
from database.config import get_settings
from auth.authanticate import authenticate_cookie
from services.crud import user as UserService


ml_router=APIRouter()
templates = Jinja2Templates(directory="view")
templates = Jinja2Templates(directory="view")
settings=get_settings()



@ml_router.post('/get_prediction', response_class=HTMLResponse)
async def get_prediction(request:Request, file: UploadFile=File(...), session=Depends(get_session)):
    token=request.cookies.get(settings.COOKIE_NAME)
    user_email = await authenticate_cookie(token)
    if token:
        if user_email:
            user = UserService.get_user_by_email(user_email,session)
            if(user):
                if(check_user_balance(user.id,session)):
                    upload_directory = "/app/shared"
                    file_location = f"{upload_directory}/{file.filename}"
                    os.makedirs(upload_directory, exist_ok=True)

                    with open(file_location, 'wb') as buffer:
                        buffer.write(file.file.read())

                    new_request = MLRequest(id=uuid.uuid4(), image=file_location, user_id=user.id)
                    create_request(new_request=new_request, session=session)
                    rabbitmq = RabbitMQ()
                    message = json.dumps(
                        {
                            "request_id": str(new_request.id), 
                        }
                    )
                    rabbitmq.send_task(message=message)
                    return templates.TemplateResponse("personal_cabinet.html", {"request": request})
                else:
                    raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail="Insufficient Funds. Increase your balance.")
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unautherised user. Please login.")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unautherised user. Please login.")





