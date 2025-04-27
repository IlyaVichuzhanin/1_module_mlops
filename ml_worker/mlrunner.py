from models.user import User
from models.request import Request
from models.response import Response
from services.crud.balance import get_balance_by_user_id, decrease_user_balance
from services.crud.price import get_current_price
from mlmodel import MLmodel
from services.crud.request import create_request
from services.crud.response import create_response
from typing import Optional
from io import BytesIO
import PIL.Image as Image
import torch
import datetime
from sqlmodel import Session
import io
import uuid

class MlRunner:

    def __init__(self):
        self.__mlmodel =MLmodel()

    @property
    def mlmodel(self):
        return self.__mlmodel
    
    def get_prediction(self, request:Request)->Optional[Response]:
        
        request_image = Image.open(request.image)
        inputs = self.__mlmodel.image_processor(request_image, return_tensors="pt")
        with torch.no_grad():
            logits = self.mlmodel.model(**inputs).logits

        predicted_label = logits.argmax(-1).item()
        response = Response(
            id=uuid.uuid4(),
            response=self.mlmodel.model.config.id2label[predicted_label],
            date_time=datetime.datetime.now(),
            user_id=request.user.id,
            user=request.user
            )

        return response


    





    