import datetime
from sqlmodel import SQLModel, Field, Relationship, LargeBinary
from typing import Optional
from sqlalchemy import Column
from typing import TYPE_CHECKING, Optional
from PIL import Image
if TYPE_CHECKING:
    from models.user import User
    from models.response import Response

class Request(SQLModel, table=True):
    __tablename__="requests"
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    image_bytes: bytes = Field(sa_column=Column(LargeBinary), default=None)
    date_time: str = Field(index=True, default=datetime.datetime.now())
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    user: Optional["User"] = Relationship(
         back_populates="requests"
    )
    response: Optional["Response"] = Relationship(back_populates="request", sa_relationship_kwargs={'uselist': False})



class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True

class CreateRequest(SQLModel, table=False):

    image_path: str  = Field(..., index=True, unique=True)
    image_bytes: Optional[bytes]  = Field(..., index=True)
    














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