from models.user import User
from models.mlmodel import MLmodel
from  models.request import Request
from  models.response import Response
from services.crud.balance import get_balance_by_user_id, decrease_user_balance
from services.crud.price import get_current_price

from services.crud.request import create_request
from services.crud.response import create_response

from typing import Optional
from io import BytesIO
import PIL.Image as Image
import torch
import datetime
from sqlmodel import Session
import io


class MlRunner:

    def __init__(self, user:User, ml_model:MLmodel):
        self.__user = user
        self.__mlmodel =ml_model

    @property
    def user(self):
        return self.__user
    
    @property
    def mlmodel(self):
        return self.__mlmodel
    
    def get_prediction(self, request:Request, session:Session)->Optional[Response]|str:
        
        if self.check_user_balance(self, session)==True:
            imageStream = io.BytesIO(request.image_bytes)
            request_image = Image.open(imageStream)
            inputs = self.__mlmodel.image_processor(request_image, return_tensors="pt")
            with torch.no_grad():
                logits = self.mlmodel.model(**inputs).logits

            predicted_label = logits.argmax(-1).item()
            response = Response(
                response=self.mlmodel.model.config.id2label[predicted_label],
                date_time=datetime.datetime.now(),
                user_id=self.user.id,
                user=self.user
            )
            
            decrease_user_balance(self.user.id, session)
            create_request(request,session)
            create_response(response, session)

            return response
        else:
            return "Balance is not enought!"

    
    def check_user_balance(self, session:Session):
        user_balance=get_balance_by_user_id(user_id=self.__user.id, session=session)
        current_price=get_current_price(session)
        if user_balance>=current_price:
            return  True
        else:
            return False




    