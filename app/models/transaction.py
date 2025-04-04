import datetime
import tkinter as tk


class Transaction:
    def __init__(self, price:float, date:datetime):
        self.__price = price
        self.__date = date
    
    @property
    def price(self):
        return self.__price
        