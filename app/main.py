from sqlmodel import SQLModel, Session, create_engine
from database.config import get_settings
from typing import TYPE_CHECKING
from fastapi import FastAPI
from sqlmodel import Session
from typing import Union
from pathlib import Path
import uvicorn
from database.database import init_db, engine
from services.crud.user import create_user, get_all_users
from models.request import Request, CreateRequest
from models.response import Response
from models.user import User
from models.mlrunner import MlRunner
from PIL import Image
import io

# from services.ml import ml as MLService
# from fastapi import APIRouter, Body, HTTPException, status, Depends
# from database.database import get_session





# create_request=CreateRequest(image_path=r'C:\Users\user\Downloads\pics_3.jpg')

# response=MLService.make_prediction(1, create_request, Depends(get_session))

# app = FastAPI(title="FastAPI, Docker, and Traefik")


# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)










        




