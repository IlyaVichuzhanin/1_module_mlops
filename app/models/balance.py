from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from typing import TYPE_CHECKING, Optional
import uuid
if TYPE_CHECKING:
    from models.user import User


class Balance(SQLModel, table=True):
    __tablename__='balances'
    id: Optional[uuid.UUID] = Field(primary_key=True, unique=True, default_factory=uuid.uuid4)
    current_balance: float = Field(index=True, default=100)
    user: Optional["User"] = Relationship(back_populates="balance", sa_relationship_kwargs={'uselist': False})


class Config:
    """ Model configuration"""
    validate_assignment=True
    arbitrary_types_allowed=True
    









