import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from typing import TYPE_CHECKING, Optional
import uuid
if TYPE_CHECKING:
    from models.user import User


class Transaction(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, unique=True, default_factory=uuid.uuid4)
    credits: float = Field(index=True, default=0)
    date_time: str = Field(index=True, default=datetime.datetime.now())
    user_id: Optional[uuid.UUID] = Field(foreign_key="users.id")
    user: Optional["User"] = Relationship(
         back_populates="transactions"
    ) 


class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True






