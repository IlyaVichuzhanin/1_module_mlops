import datetime
import uuid
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func


class Transaction(SQLModel, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)
    credits: float
    date_time: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    user_id: uuid.UUID  = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="transactions")

    class Config:
        arbitrary_types_allowed = True





