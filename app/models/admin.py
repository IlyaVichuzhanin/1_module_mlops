import datetime
from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from models.user import User
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg



class Admin(SQLModel, table=True):
    id: UUID = Field(primary_key=True, unique=True, default=uuid4)
    email: str = Field(index=True)
    password: str = Field(index=True)






