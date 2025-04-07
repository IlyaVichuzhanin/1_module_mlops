import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
#from models.user import User


class Response(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    response: str
    response_date_time: datetime
    user_id: int = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="responces")



















# import datetime
# from tkinter import Image


# class response:


#     def __init__(self, response:str, responseDateTime:datetime):
#         self.__response = response
#         self.__responseDateTime = responseDateTime
    
#     @property
#     def response(self):
#         return self.__response
    
#     @property
#     def responseDateTime(self):
#         return self.__responseDateTime