import datetime
from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class Balance(SQLModel, table=True):
    #__tablename__="balance"
    id: UUID = Field(sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4))
    current_balance: float
    user_id: int = Field(foreign_key="user.id", unique=True)
    user: "User" = Relationship(back_populates="balance")


class Config:
    arbitrary_types_allowed = True








