from typing import Optional, List
from models.transaction import Transaction
from models.request import Request
from models.response import Response
from models.balance import Balance
from sqlmodel import SQLModel, Field, Relationship


class Admin(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None)
    password: str = Field(default=None)
    transactions: Optional[List[Transaction]] = Relationship(back_populates="admins")
    requests: Optional[List[Request]] = Relationship(back_populates="admins")
    responses: Optional[List[Response]] = Relationship(back_populates="admins")






