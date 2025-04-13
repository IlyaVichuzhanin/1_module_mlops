import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey, Integer
from typing import Optional, List
import uuid
import sqlalchemy.dialects.postgresql as pg
from typing import TYPE_CHECKING, Optional, List
if TYPE_CHECKING:
    from models.user import User


class Balance(SQLModel, table=True):
    __tablename__='balances'
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    current_balance: float = Field(index=True, default=0)
    user_id: int = Field(sa_column=Column(Integer, ForeignKey("users.id", ondelete="SET NULL", onupdate="CASCADE")))









