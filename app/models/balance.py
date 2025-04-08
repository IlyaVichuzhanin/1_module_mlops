import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.user import User


class Balance(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    current_balance: float
    user_id: int = Field(foreign_key="user.id", unique=True)
    user: User = Relationship(back_populates="balance")










