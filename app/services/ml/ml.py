from  models.mlmodel import MLmodel
from models.mlrunner import MlRunner
from  models.user import User
from  models.request import Request, CreateRequest
from  models.response import Response
from typing import List, Optional
from sqlmodel import Session
from services.crud.user import get_user_by_id



def make_prediction(user_id:int, create_request:CreateRequest, ml_model:MLmodel, session:Session) -> Optional[Response]:
    user = get_user_by_id(user_id, session)
    ml_runner = MlRunner(user=user, ml_model=ml_model)
    imageFileObj = open(create_request.image_path, "rb")
    imageBinaryBytes = imageFileObj.read()
    request = Request(image_bytes=imageBinaryBytes, user_id=user.id, user=user)
    response = ml_runner.get_prediction(request, session)
    if response:
        return response
    else:
        return None
    


