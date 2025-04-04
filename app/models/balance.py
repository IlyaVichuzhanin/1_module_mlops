from models.transaction import Transaction

class Balance:
    def __init__(self):
        self.__currentBalance=0

    @property
    def currentBalance(self):
        return self.__currentBalance
    
    def increaseBalance(self, transaction:Transaction):
        if transaction.credits>=0:
            self.__currentBalance+=transaction.credits
        else:
            return "Недопустимое значение"
    
    def decreaseBalance(self, transaction:Transaction):
        if transaction.credits<0:
            return "Недопустимое значение"
        elif (self.__currentBalance<transaction.credits):
            return "Недостаточно средств на балансе"
        else:
            self.__currentBalance-=transaction.credits
        

    