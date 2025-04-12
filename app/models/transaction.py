import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class Transaction(SQLModel, table=True):
    #__tablename__="transactions"
    id: UUID = Field(sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4))
    credits: float
    date_time: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    user_id: UUID  = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="transactions")

    class Config:
        arbitrary_types_allowed = True





