from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from models.balance import Balance
if TYPE_CHECKING:
    from models.transaction import Transaction
    from models.response import Response
    from models.request import Request
    





class User(SQLModel, table=True):
    __tablename__='users'
    id: int = Field(primary_key=True, unique=True, default=None)
    email: str  = Field(..., index=True, unique=True)
    hashed_password: bytes  = Field(..., index=True)
    balance_id: Optional[int] = Field(foreign_key="balances.id", default=None)
    balance: Optional["Balance"] = Relationship(back_populates="user")
    transactions: Optional[list["Transaction"]] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"
            }
        )
    requests: Optional[list["Request"]] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"
            }
        )
    responses: Optional[list["Response"]] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"
            }
        )
    

class SignUpUser(SQLModel, table=False):
    email: Optional[str]  = Field(..., index=True, unique=True)
    password: Optional[str]  = Field(..., index=True)

class SignInUser(SQLModel, table=False):
    email: Optional[str]  = Field(..., index=True, unique=True)
    password: Optional[str]  = Field(..., index=True)

    
    
    
class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True





    

