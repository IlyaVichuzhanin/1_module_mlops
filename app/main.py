
from typing import TYPE_CHECKING
import uuid
from fastapi import FastAPI
from sqlmodel import Session
from typing import Union
from pathlib import Path
import uvicorn
from database.database import init_db, engine
from services.crud.user import create_user, get_all_users
from models.user import User
from models.transaction import Transaction 
from services.crud.balance import create_balance, increase_user_balance, decrease_user_balance  


app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get('/')
def index():
   return {'message': 'Everything online'}


if __name__ == "__main__":
    test_user1 =  User(id=uuid.uuid1,email="Bob@yandex.ru", password="123")
    test_user2 = User(id=uuid.uuid1,email="Jane@yandex.ru", password="123")

    init_db()
    print("Init db has been succeded")

    with Session(engine) as session:
        create_user(test_user1, session)
        create_user(test_user2, session)
        users=get_all_users(session)
    
        for user in users:
            print(f'id: {user.id} - {user.email}')
            print(type(user))

    with Session(engine) as session:
        test_transaction_1=Transaction(id=uuid.uuid1, credits=54, date_time='11.05.2025', user_id=test_user1.id, user=test_user1)
        increase_user_balance(test_user1, test_transaction_1)
        test_transaction_2=Transaction(id=uuid.uuid1, credits=8, date_time='13.06.2025', user_id=test_user1.id, user=test_user1)
        decrease_user_balance(test_user1, test_transaction_2)
        test_transaction_3=Transaction(id=uuid.uuid1, credits=100, date_time='16.07.2025', user_id=test_user1.id, user=test_user1)
        decrease_user_balance(test_user1, test_transaction_3)


        




