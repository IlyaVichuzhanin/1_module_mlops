from fastapi import APIRouter, Body, HTTPException, status, Depends, File, UploadFile, Form, Request, Response
from database.database import get_session
from models.user import User
from models.response import Response
from services.crud.user import get_user_by_id
from services.crud.balance import check_user_balance, get_balance_by_user_id
from services.crud.request import create_request
from services.crud.response import get_response_by_request_id
from typing import List
import os
from services.rm.rabbitmq import RabbitMQ
import json
import uuid
import time
from forms.uploadimageform import UploadImageForm
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.request import Request as MLRequest


ml_router=APIRouter()
templates = Jinja2Templates(directory="view")



@ml_router.post('/get_prediction', response_class=HTMLResponse)
async def get_prediction(request:Request, file: UploadFile=File(...), session=Depends(get_session)):
    user_id="773e3742-c9ae-4f10-85d8-da3d0d3490b6"
    form = UploadImageForm(request)
    await form.load_data()
    if(check_user_balance(uuid.UUID(user_id),session)):
        
        upload_directory = "/app/shared"
        file_location = f"{upload_directory}/{file.filename}"
        os.makedirs(upload_directory, exist_ok=True)

        with open(file_location, 'wb') as buffer:
            buffer.write(file.file.read())

        new_request = MLRequest(id=uuid.uuid4(), image=file_location, user_id=user_id)
        create_request(new_request=new_request, session=session)
        rabbitmq = RabbitMQ()
        message = json.dumps(
            {
                "request_id": str(new_request.id), 
            }
        )
        rabbitmq.send_task(message=message)
    return templates.TemplateResponse("personal_cabinet.html", {"request": request})





