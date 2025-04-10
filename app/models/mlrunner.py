from models.transaction import Transaction
from models.request import Request
from models.user import User
from models.mlmodel import MLmodel


class MlRunner:

    def __init__(self, user:User, mlmodel:MLmodel):
        self.__user = user
        self.__mlmodel = mlmodel

    @property
    def user(self):
        return self.__user
    
    @property
    def mlmodel(self):
        return self.__mlmodel

    def makePrediction(self, mlmodel:MLmodel, request:Request):
        pass

    def validateRequestData(self, request:Request):
        pass


    