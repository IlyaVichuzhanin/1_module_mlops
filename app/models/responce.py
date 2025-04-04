import datetime
from tkinter import Image


class Responce:


    def __init__(self, responce:Image, responceDateTime:datetime):
        self.__responce = responce
        self.__responceDateTime = responceDateTime
    
    @property
    def responce(self):
        return self.__responce
    
    @property
    def responceDateTime(self):
        return self.__responceDateTime