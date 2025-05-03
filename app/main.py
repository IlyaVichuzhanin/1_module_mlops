# from sqlmodel import SQLModel, Session, create_engine
# from database.config import get_settings
# from typing import TYPE_CHECKING
# from fastapi import FastAPI
# from sqlmodel import Session
# from typing import Union
# from pathlib import Path
# import uvicorn
# from database.database import init_db, engine
# from services.crud.user import create_user, get_all_users
# from models.request import Request, CreateRequest
# from models.response import Response
# from models.user import SignUpUser
# from PIL import Image
# import io
# import json
# import uuid


from PIL import Image
import requests
from transformers import AutoProcessor, BlipForConditionalGeneration, BlipProcessor


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(r'C:\Users\user\Downloads\Blog-vtoroysvet-1300x650-07.jpg').convert('RGB')
text = "a photography of"
inputs = processor(image, return_tensors="pt")

outputs = model.generate(**inputs)

print(processor.decode(outputs[0], skip_special_tokens=True))

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")









        




