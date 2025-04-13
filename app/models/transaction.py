import datetime
import uuid
from sqlmodel import SQLModel, Field, Relationship, ForeignKey, Integer
from typing import Optional, List
from sqlalchemy import Column, DateTime, func
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
from typing import TYPE_CHECKING, Optional, List
if TYPE_CHECKING:
    from models.user import User


class Transaction(SQLModel, table=True):
    __tablename__='transactions'
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    credits: float = Field(index=True, default=0)
    date_time: str = Field(index=True, default=datetime.datetime.now())
    user_id: Optional[int] = Field(sa_column=Column(Integer, ForeignKey("users.id", ondelete="SET NULL", onupdate="CASCADE")))






