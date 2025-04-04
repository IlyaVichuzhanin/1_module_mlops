from models.transaction import Transaction
from models.request import Request
from models.responce import Responce
from models.balance import Balance
import datetime
import bcrypt


class User:

    def __init__(self, userName:str, email:str, my_password:str) -> None:
        self.__userName = userName
        self.__email = email
        self.__password = bcrypt.hashpw(password=my_password, salt=bcrypt.gensalt())
        self.__list_transaction = [Transaction]
        self.__list_request = [Request]
        self.__list_responce = [Responce]
        self.__creditBalance = Balance
    
    @property
    def userName(self):
        return self.__userName

    @property
    def email(self):
        return self.__email
    
    @property
    def transactions(self):
        return self.__list_transaction

    @property
    def requests(self):
        return self.__list_request
    
    @property
    def responce(self):
        return self.__list_responce

    @property
    def creditBalance(self):
        return self.__creditBalance   

    def __str__(self) -> str:
        return "{self.id} + {self.email}"

    def authorise(self, emailOrUserName:str, password:str):
        pass

    def register(self, userName:str, email:str, password:str):
        pass

    def exit(self):
        pass   
        


