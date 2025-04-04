from models.transaction import Transaction

class Balance:
    def __init__(self):
        self.__currentBalance=0

    @property
    def currentBalance(self):
        return self.__currentBalance

    def increaseBalance(self, transaction:Transaction):
        if credits>=0:
            self.__currentBalance+=transaction.price
        else:
            return "Недопустимое значение"
    
    def decreaseBalance(self, transaction:Transaction):
        if credits>=0:
            self.__currentBalance-=transaction.price
        else:
            return "Недопустимое значение"