
from typing import TYPE_CHECKING
from fastapi import FastAPI
from sqlmodel import Session
import uvicorn
if TYPE_CHECKING:
    from database.database import init_db, engine
    from services.crud.user import create_user, get_all_users
    from models.user import User


# app=FastAPI()

# @app.get('/')

# def index():
#     user_nick = User("123", "123", "123")
#     return "Hello world!" + str(user_nick)w


# if __name__ == "__main__":
#     uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)


if __name__ == "__main__":
    test_user = User(id=1,user_name="Bob", password="123")
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




