import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func

class Request(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    image: bytes
    date_time: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    user_id: int = Field(default=None, foreign_key="user.id")
    user: "User"  = Relationship(back_populates="requests")
    
    class Config:
        arbitrary_types_allowed = True













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