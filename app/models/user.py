from sqlmodel import SQLModel, Field, Relationship, Column
from typing import TYPE_CHECKING, Optional, List
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
if TYPE_CHECKING:
    from models.transaction import Transaction
    from models.response import Response
    from models.request import Request
    from models.balance import Balance


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(primary_key=True, unique=True, default=uuid4)
    email: str = Field(index=True)
    password: str = Field(index=True)
    transactions: List["Transaction"] = Relationship(back_populates="user")
    requests: List["Request"] = Relationship(back_populates="user")
    responses: List["Response"] = Relationship(back_populates="user")
    balance: "Balance" = Relationship(back_populates="user")
    
    # class Config:
    #     arbitrary_types_allowed = True
    

