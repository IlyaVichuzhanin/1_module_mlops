import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.user import User


class Request(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    image: bytearray
    date_time: datetime
    user_id: int = Field(default=None, foreign_key="user.id")
    user: User  = Relationship(back_populates="requests")













# import datetime
# from tkinter import Image


# class Request:

#     def __init__(self, request:Image, requestDateTime:datetime):
#         self.__request = request
#         self.__requestDateTime = requestDateTime
    
#     @property
#     def request(self):
#         return self.__request
    
#     @property
#     def requestDateTime(self):
#         return self.__requestDateTime