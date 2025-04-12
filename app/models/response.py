import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg

class Response(SQLModel, table=True):
    #__tablename__="responses"
    id: UUID = Field(sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4))
    response: str
    date_time: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    user_id: UUID = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="responses")
    
    class Config:
        arbitrary_types_allowed = True
















