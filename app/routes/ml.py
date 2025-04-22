from fastapi import APIRouter, Body, HTTPException, status, Depends, File, UploadFile
from database.database import get_session
from models.user import User
from models.request import Request, CreateRequest
from models.response import Response
from services.crud.user import get_user_by_id
from services.crud.balance import check_user_balance
from services.crud.request import create_request
from typing import List
import os
from services.rm.rabbitmq import RabbitMQ
import json


ml_router=APIRouter()
#ml_model = MLmodel()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR=os.path.join(BASE_DIR, "uploads")


# @ml_router.post(
#         '/make_prediction',  
#         response_model=Response,
#         summary="ML endpoint",
#         description="Send ml request"
#         )
# async def make_prediction(user_id:int, create_request:CreateRequest, session=Depends(get_session))->Response:


@ml_router.post("/file/upload")
def upload_file(user_id:int, new_image_file: UploadFile=File(...), session=Depends(get_session))->Response | dict:
    
    if(check_user_balance(user_id,session)):
        return {'message': 'Balance is not enought'}
    else:
        upload_directory = "./uploads"
        file_location = f"./{upload_directory}/{new_image_file.filename}"
        os.makedirs(upload_directory, exist_ok=True)

        with open(file_location, 'wb') as buffer:
            buffer.write(new_image_file.file.read())

        
        

        rabbitmq = RabbitMQ()
        message = json.dumps(
            {
                "user_id": user_id, 
                "image_path": file_location 
            }
        )
        rabbitmq.send_task(message=message)





    #data = new_image_file.file.read()
    








# @ml_router.post(
#         '/make_prediction',  
#         response_model=Response,
#         summary="ML endpoint",
#         description="Send ml request"
#         )
# async def make_prediction(user_id:int, create_request:CreateRequest, session=Depends(get_session))->Response:
    
#     response=MLService.make_prediction(user_id, create_request, ml_model, session)
#     if response is None:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Model prediction has failed.")
#     else:
#         return response


