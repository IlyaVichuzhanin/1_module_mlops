from  models.mlmodel import MLmodel
from models.mlrunner import MlRunner
from  models.user import User
from  models.request import Request
from  models.response import Response
from typing import List, Optional
from sqlmodel import Session




def make_prediction(user:User, request:Request, session:Session) -> Optional[Response]:
    ml_runner = MlRunner(user)
    response = ml_runner.get_prediction(request, session)
    if response:
        return response
    else:
        return None
    


