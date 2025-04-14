import datetime
import uuid
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Balance(SQLModel, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)
    current_balance: float
    user_id: uuid.UUID = Field(foreign_key="user.id", unique=True)
    user: "User" = Relationship(back_populates="balance")


class Config:
    arbitrary_types_allowed = True








