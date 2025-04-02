from models.transaction import Transaction
from models.user import User


class Admin:

    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

    def authorizeAdmin(self, email:str, password:str):
        pass

    def registerAdmin(self, email:str, password:str):
        pass

    def showUserTransactions(self, user:User):
        pass

    def showUserPredictions(self, user:User):
        pass

    def increaseCreditBalance(self, user:User, transaction:Transaction):
        user.creditBalance+=transaction.credits
        