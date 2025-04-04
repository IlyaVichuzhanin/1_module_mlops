import datetime
from tkinter import Image


class Request:


    def __init__(self, request:Image, requestDateTime:datetime):
        self.__request = request
        self.__requestDateTime = requestDateTime
    
    @property
    def request(self):
        return self.__request
    
    @property
    def requestDateTime(self):
        return self.__requestDateTime