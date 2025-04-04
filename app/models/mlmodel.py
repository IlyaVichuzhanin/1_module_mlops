from transformers import (AutoTokenizer, AutoModelForSequenceClassification, 
                          TrainingArguments, Trainer)


class MLmodel:

    def __init__(self, urlPath:str, num_labels:int):
        self.__model= AutoModelForSequenceClassification.from_pretrained(urlPath,num_labels)

    @property
    def model(self):
        return self.__model
    