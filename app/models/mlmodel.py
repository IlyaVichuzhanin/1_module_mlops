import torch
from PIL import Image

import requests
from transformers import AutoImageProcessor, AutoModelForImageClassification, ViTForImageClassification


class MLmodel:

    def __init__(self):
        self.__model= AutoModelForImageClassification.from_pretrained("victor/animals-classifier")
        self.__image_processor = AutoImageProcessor.from_pretrained("victor/animals-classifier")


    @property
    def model(self):
        return self.__model
    
    @property
    def image_processor(self):
        return self.__image_processor
    