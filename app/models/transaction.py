import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.user import User


class Transaction(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    credits: float
    date_time: datetime
    user_id: int  = Field(default=None, foreign_key="user.id")
    user: User  = Relationship(back_populates="transactions")











# import datetime
# import tkinter as tk


# class Transaction:
#     def __init__(self, credits:float, dateTime:datetime):
#         self.__credits = credits
#         self.__dateTime = dateTime
    
#     @property
#     def credits(self):
#         return self.__credits
        