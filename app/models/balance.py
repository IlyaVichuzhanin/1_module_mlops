import datetime
from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
from typing import TYPE_CHECKING, Optional, List
if TYPE_CHECKING:
    from models.user import User


class Balance(SQLModel, table=True):
    id: UUID = Field(primary_key=True, unique=True, default=uuid4)
    current_balance: float = Field(index=True, default=0)
    user_id: UUID = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="balance")


class Config:
    arbitrary_types_allowed = True








