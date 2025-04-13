from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey, Integer
from typing import TYPE_CHECKING, Optional, List
import uuid
import sqlalchemy.dialects.postgresql as pg
if TYPE_CHECKING:
    from models.transaction import Transaction
    from models.response import Response
    from models.request import Request
    from models.balance import Balance


class User(SQLModel, table=True):
    __tablename__='users'
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    email: str = Field(index=True)
    password: str = Field(index=True)

    

