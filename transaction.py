import datetime
import tkinter as tk


class Transaction:
    def __init__(self, credits:int, date:datetime):
        self.credits = credits
        self.date = date
        