from fastapi import APIRouter, Body, HTTPException, status, Depends, File, UploadFile
from database.database import get_session
from models.user import User
from models.request import Request, CreateRequest
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


ml_router=APIRouter()



@ml_router.post("/file/get_prediction")
def get_prediction(user_id:str, new_image_file: UploadFile=File(...), session=Depends(get_session))->None:
    
    if(check_user_balance(uuid.UUID(user_id),session)):
        
        upload_directory = "/app/shared"
        file_location = f"{upload_directory}/{new_image_file.filename}"
        os.makedirs(upload_directory, exist_ok=True)

        with open(file_location, 'wb') as buffer:
            buffer.write(new_image_file.file.read())

        new_request = Request(id=uuid.uuid4(), image=file_location, user_id=user_id)
        create_request(new_request=new_request, session=session)
        rabbitmq = RabbitMQ()
        message = json.dumps(
            {
                "request_id": str(new_request.id), 
            }
        )
        rabbitmq.send_task(message=message)

        # timeout=15000
        # start_time=time.time()
        # while True:
        #     response=get_response_by_request_id(request_id=new_request.id, session=session)
        #     if response:
        #         return response
        #     elif (time.time()-start_time)>timeout:
        #         return {'message': 'Time_out_service'}

    else:
        return {'message': 'Balance is not enought'}




