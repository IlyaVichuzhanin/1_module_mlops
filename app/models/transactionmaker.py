from models.user import User
from models.transaction import Transaction



class TransactionMaker:

    def __init__(self, user:User):
        self.__user=user
    
    def increaseBalance(self, transaction:Transaction):
        # self.__user.creditBalance.increaseBalance(transaction)
        pass

    def decreaseBalance(self, transaction:Transaction):
        # self.__user.creditBalance.decreaseBalance(transaction)
        pass


    
        