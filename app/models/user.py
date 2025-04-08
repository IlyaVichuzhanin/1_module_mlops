from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from models.transaction import Transaction
from models.request import Request
from models.response import Response
from models.balance import Balance


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None)
    password: str = Field(default=None)
    transactions: Optional[List[Transaction]] = Relationship(back_populates="user")
    requests: Optional[List[Request]] = Relationship(back_populates="user")
    responses: Optional[List[Response]] = Relationship(back_populates="user")
    balance: Optional[Balance] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})
    

