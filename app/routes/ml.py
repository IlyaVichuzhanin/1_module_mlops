from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from models.request import Request
from models.response import Response
from services.crud import user as UserService
from services.ml import ml as MLService
from services.crud import request as RequestService
from services.crud import response as ResponseService
from typing import List
from py_linq import Enumerable


ml_router=APIRouter()



@ml_router.get('/make_prediction',  response_model=Response)
async def make_prediction(user:User, request:Request, session=Depends(get_session))->List:
    if MLService.make_prediction(user, request, session=Depends(get_session)) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Model prediction has failed.")



# @ml_route.post(
#     "/send_task",
#     response_model=Dict[str,str],
#     summary="ML endpoint",
#     description="Send ml request"
# )

# async def index(message:str)->str:
#     """
#     Root endpoint returning welcome message.
#     Returns:
#         Dict[str,str]: Welcome message
#     """
#     try:
#         send_task(message)
#         return {"message": f"Task sent successfully!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=e)