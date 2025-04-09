from typing import Optional, List
import uuid
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)
    email: str = Field(default=None)
    password: str = Field(default=None)
    transactions: Optional[List["Transaction"]] = Relationship(back_populates="user")
    requests: Optional[List["Request"]] = Relationship(back_populates="user")
    responses: Optional[List["Response"]] = Relationship(back_populates="user")
    balance: Optional["Balance"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})
    
    class Config:
        arbitrary_types_allowed = True
    

