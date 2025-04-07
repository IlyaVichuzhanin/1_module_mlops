from typing import Optional, List
from models.transaction import Transaction
from models.request import Request
from models.response import Response
from models.balance import Balance
from sqlmodel import SQLModel, Field, Relationship


class Admin(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None)
    password: str = Field(default=None)
    transactions: Optional[List[Transaction]] = Relationship(back_populates="admins")
    requests: Optional[List[Request]] = Relationship(back_populates="admins")
    responses: Optional[List[Response]] = Relationship(back_populates="admins")












# from models.transaction import Transaction
# from models.user import User



# class Admin(User):

#     def __init__(self, email:str, password:str):
#         self.email = email
#         self.password = password

#     def authorizeAdmin(self, email:str, password:str):
#         pass

#     def registerAdmin(self, email:str, password:str):
#         pass

#     def showUserTransactions(self, user:User):
#         pass

#     def showUserPredictions(self, user:User):
#         pass

#     def increaseCreditBalance(self, user:User, transaction:Transaction):
#         # user.creditBalance.increaseBalance(transaction)
#         pass