import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
from typing import TYPE_CHECKING, Optional


class Price(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    credits: float = Field(index=True, default=0)
    date_time: str = Field(index=True, default=datetime.datetime.now())


class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True