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
from models.request import Request
from models.response import Response
from models.user import User
from PIL import Image

# app = FastAPI(title="FastAPI, Docker, and Traefik")


# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)



# if __name__=="__main__":
#     test_user =  User(email="Bob@yandex.ru", password="123")
#     test_user2 = User(email="Jane", password="123")



# import logging

# logger = logging.getLogger(__name__)


# app = FastAPI(title="FastAPI, Docker, and Traefik")


# @app.get('/')
# def index():
#     return {'message': 'Everything online'}


# @app.on_event("startup")
# def on_startup():
#     init_db()
#     logger.info("Init db has been succeeded")

#     # test_user =  User(email="Bob@yandex.ru", password="123")
#     # test_user2 = User(email="Jane", password="123")
#     # create_user(test_user)
#     # create_user(test_user2)

#     with Session(engine) as session:
#         test_user =  User(email="Bob@yandex.ru", password="123")
#         #test_user2 = User(email="Jane", password="123")
#         create_user(test_user, session)
#         #create_user(test_user2, session)
#         #users = get_all_users(session)
#         #for user in users:
#         #    logger.info(f'id: {user.id} - {user.email}')

        




