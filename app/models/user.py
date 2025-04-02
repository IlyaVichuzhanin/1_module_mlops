from models.transaction import Transaction
from models.prediction import Prediction
import datetime


class User:

    def __init__(self, userName:str, email:str, password:str) -> None:
        self.userName = userName
        self.email = email
        self.password = password
        self.list_transaction = [Transaction]
        self.list_prediction = [Prediction]
        self.creditBalance = 0

    def __str__(self) -> str:
        return "{self.id} + {self.email}"

    def authoriseUser(self, emailOrUserName:str, password:str):
        pass

    def registerUser(self, userName:str, email:str, password:str):
        pass

    def increasBalance(self, transaction:Transaction):
        self.creditBalance+=transaction.credits

    def exit(self):
        pass   
        


