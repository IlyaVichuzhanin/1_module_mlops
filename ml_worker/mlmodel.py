from transformers import AutoImageProcessor, AutoModelForImageClassification




class MLmodel:

    def __init__(self):
        self.__model= AutoImageProcessor.from_pretrained("dima806/facial_emotions_image_detection")
        self.__image_processor = AutoModelForImageClassification.from_pretrained("dima806/facial_emotions_image_detection")


    @property
    def model(self):
        return self.__model
    
    @property
    def image_processor(self):
        return self.__image_processor
    