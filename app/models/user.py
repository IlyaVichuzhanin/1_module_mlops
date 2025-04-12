from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, Column
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class User(SQLModel, table=True):
    #__tablename__="users"
    id: UUID = Field(sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4))
    email: str = Field(default=None)
    password: str = Field(default=None)
    transactions: Optional[List["Transaction"]] = Relationship(back_populates="user")
    requests: Optional[List["Request"]] = Relationship(back_populates="user")
    responses: Optional[List["Response"]] = Relationship(back_populates="user")
    balance: Optional["Balance"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})
    
    class Config:
        arbitrary_types_allowed = True
    

