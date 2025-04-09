import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func

class Response(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    response: str
    date_time: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    user_id: int = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="responses")
    
    class Config:
        arbitrary_types_allowed = True
















