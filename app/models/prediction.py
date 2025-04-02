import datetime
from tkinter import Image
from models.transaction import Transaction 


class Prediction:

    mlResponce :str

    def __init__(self, request:Image, requestDateTime:datetime, transaction:Transaction):
        self.request = request
        self.requestDateTime = requestDateTime
        self.transaction = transaction