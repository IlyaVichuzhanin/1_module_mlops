import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.user import User



class Admin(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None)
    password: str = Field(default=None)






