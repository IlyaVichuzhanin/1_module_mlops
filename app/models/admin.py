from sqlmodel import SQLModel, Field
from typing import Optional



class Admin(SQLModel, table=True):
    __tablename__='admins'
    id: Optional[int] = Field(primary_key=True, unique=True, default=None)
    email: str = Field(index=True)
    password: str = Field(index=True)






