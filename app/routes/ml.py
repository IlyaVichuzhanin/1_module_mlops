from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from models.request import Request, CreateRequest
from models.response import Response
from services.ml import ml as MLService
from services.crud.user import get_user_by_id
from typing import List
from models.mlmodel import MLmodel


ml_router=APIRouter()
ml_model = MLmodel()


@ml_router.post(
        '/make_prediction',  
        response_model=Response,
        summary="ML endpoint",
        description="Send ml request"
        )
async def make_prediction(user_id:int, create_request:CreateRequest, session=Depends(get_session))->Response:
    
    response=MLService.make_prediction(user_id, create_request, ml_model, session)
    if response is None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Model prediction has failed.")
    else:
        return response

