import datetime
import tkinter as tk


class Transaction:
    def __init__(self, credits:float, dateTime:datetime):
        self.__credits = credits
        self.__dateTime = dateTime
    
    @property
    def credits(self):
        return self.__credits
        