from  models.mlmodel import MLmodel
from models.mlrunner import MlRunner
from  models.user import User
from  models.request import Request
from  models.response import Response
from typing import List, Optional
from services.crud.transaction import provide_transaction




def make_prediction(user:User, request:Request, session) -> Optional[Response]:
    ml_runner = MlRunner(user)
    response = ml_runner.get_prediction(request)
    if response:
        provide_transaction(user, session)
        return response
    else:
        return None
    


