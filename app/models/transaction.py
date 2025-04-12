import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, DateTime, func
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
from typing import TYPE_CHECKING, Optional, List
if TYPE_CHECKING:
    from models.user import User


class Transaction(SQLModel, table=True):
    id: Optional[UUID] = Field(primary_key=True, unique=True, default=uuid4)
    credits: float = Field(index=True, default=0)
    date_time: str = Field(index=True, default=datetime.datetime.now())
    user_id: UUID = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="transactions")

    # class Config:
    #     arbitrary_types_allowed = True





