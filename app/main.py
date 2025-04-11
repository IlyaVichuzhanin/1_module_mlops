from sqlmodel import SQLModel, Session, create_engine
from database.config import get_settings



engine = create_engine(url=get_settings().DATABASE_URL_psycopg, echo=True,pool_size=5, max_overflow=10)




from typing import TYPE_CHECKING
from fastapi import FastAPI
from sqlmodel import Session
from typing import Union
from pathlib import Path
import uvicorn
from database.database import init_db, engine
from services.crud.user import create_user, get_all_users
from models.user import User
    


app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get('/')
def index():
   return {'message': 'Everything online'}


if __name__ == "__main__":
    test_user =  User(id=1,email="Bob@yandex.ru", password="123")
    test_user2 = User(id=1,user_name="Jane", password="123")

    init_db()
    print("Init db has been succeded")

    with Session(engine) as session:
        create_user(test_user, session)
        create_user(test_user2, session)
        users=get_all_users(session)
    
        for user in users:
            print(f'id: {user.id} - {user.email}')
            print(type(user))

        




