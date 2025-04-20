from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from models.request import Request, CreateRequest
from models.response import Response
from services.ml import ml as MLService
from typing import List


ml_router=APIRouter()



@ml_router.post('/make_prediction',  response_model=Response)
async def make_prediction(user_id:int, request:CreateRequest, session=Depends(get_session))->List:
    imageFileObj = open(request.image_path, "rb")
    imageBinaryBytes = imageFileObj.read()
    request.image_bytes=imageBinaryBytes
    response=MLService.make_prediction(user_id, request, session)
    if response is None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Model prediction has failed.")
    else:
        return response

