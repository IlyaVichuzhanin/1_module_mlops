from models.user import User
from models.mlmodel import MLmodel
from  models.request import Request
from  models.response import Response
from typing import Optional
from io import BytesIO
import PIL.Image as Image
import torch
import datetime


class MlRunner:

    def __init__(self, user:User):
        self.__user = user
        self.__mlmodel = MLmodel()

    @property
    def user(self):
        return self.__user
    
    @property
    def mlmodel(self):
        return self.__mlmodel
    
    def get_prediction(self, request:Request)->Optional[Response]:
        request_image = Image.open(BytesIO(request.image))
        inputs = self.__mlmodel.image_processor(request_image, return_tensors="pt")
        with torch.no_grad():
            logits = self.__mlmodel(**inputs).logits
        
        predicted_label = logits.argmax(-1).item()
        response = Response(
            response=self.__mlmodel.config.id2label[predicted_label],
            date_time=datetime.datetime.now(),
            user_id=self.user.id,
            user=self.user)
        return response



    