import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
from typing import TYPE_CHECKING, Optional
import uuid


class Price(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, unique=True, default_factory=uuid.uuid4)
    credits: float = Field(index=True, default=0)
    date_time: str = Field(index=True, default=datetime.datetime.now())


class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True