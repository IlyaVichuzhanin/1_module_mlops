import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey, Integer
from typing import Optional, List
import uuid
import sqlalchemy.dialects.postgresql as pg
from typing import TYPE_CHECKING, Optional, List
if TYPE_CHECKING:
    from models.user import User
    from models.balance import Balance


class Balance(SQLModel, table=True):
    __tablename__='balances'
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    current_balance: float = Field(index=True, default=0)
    balance_id: Optional[int] = Relationship(back_populates="balance_id", sa_relationship_kwargs={"lazy": "selectin"})
    balance: Optional["Balance"] = Relationship(back_populates="balance", sa_relationship_kwargs={"lazy": "selectin"})


class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True
    









