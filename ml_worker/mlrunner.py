


from app.models.user import User
from app.models.request import Request
from app.models.response import Response
from app.services.crud.balance import get_balance_by_user_id, decrease_user_balance
from app.services.crud.price import get_current_price
from mlmodel import MLmodel

from app.services.crud.request import create_request
from app.services.crud.response import create_response

from typing import Optional
from io import BytesIO
import PIL.Image as Image
import torch
import datetime
from sqlmodel import Session
import io




class MlRunner:

    def __init__(self):
        self.__mlmodel =MLmodel()

    
    @property
    def mlmodel(self):
        return self.__mlmodel
    
    def get_prediction(self, image_path:str, user:User)->Optional[Response]:
        
        request_image = Image.open(image_path)
        inputs = self.__mlmodel.image_processor(request_image, return_tensors="pt")
        with torch.no_grad():
            logits = self.mlmodel.model(**inputs).logits

        predicted_label = logits.argmax(-1).item()
        response = Response(
            response=self.mlmodel.model.config.id2label[predicted_label],
            date_time=datetime.datetime.now(),
            user_id=user.id,
            user=user
        )

        return response


    





    