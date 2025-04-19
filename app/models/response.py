import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from models.user import User
    from models.request import Request

class Response(SQLModel, table=True):
    __tablename__="responses"
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    response: str= Field(index=True)
    date_time: str = Field(index=True, default=datetime.datetime.now())
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    user: Optional["User"] = Relationship(
         back_populates="responses"
    )
    request_id: Optional[int] = Field(foreign_key="requests.id", default=None)
    request: Optional["Request"] = Relationship(back_populates="response")

class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True
















