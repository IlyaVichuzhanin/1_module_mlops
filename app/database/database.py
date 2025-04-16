from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from database.config import get_settings
from models.user import User
from models.admin import Admin
from models.transaction import Transaction
from models.request import Request
from models.response import Response

from services.crud.user import create_user
from services.crud.admin import create_admin
from services.crud.transaction import create_transaction
from services.crud.request import create_request
from services.crud.response import create_response


engine = create_engine(url=get_settings().DATABASE_URL_psycopg, echo=True,pool_size=5, max_overflow=10)


def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    

    # test_user_1 = User(email="Bob", password="123")
    # test_user_2 = User(email="Sam", password="123")
    # test_user_3 = User(email="Alice", password="123")
    # test_admin_1 = Admin(email="Jack", password="123")
    # test_transaction_1=Transaction(credits=12, date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)
    # test_response_1 = Response(response="some response", date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)
    # test_request_1 = Request(image=bytearray, date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)

        
    # create_user(test_user_1,get_session())
    # create_user(test_user_2,get_session())
    # create_user(test_user_3,get_session())
    # create_admin(test_admin_1,get_session())
    # create_transaction(test_transaction_1,get_session())
    # create_response(test_response_1,get_session())
    # create_request(test_request_1,get_session())

    




