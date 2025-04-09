import uuid
from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from .config import get_settings
from models.user import User
from models.admin import Admin
from models.transaction import Transaction
from models.request import Request
from models.response import Response
from models.balance import Balance
from services.crud.user import create_user
from services.crud.admin import create_admin
from services.crud.transaction import create_transaction
from services.crud.request import create_request
from services.crud.responses import create_response
from services.crud.balance import create_balance, increase_user_balance, decrease_user_balance

engine = create_engine(url=get_settings().DATABASE_URL_psycopg, echo=True,pool_size=5, max_overflow=10)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    test_user_1 = User(id=uuid.uuid1,email="Bob", password="123")
    create_user(test_user_1, get_session)
    test_user_2 = User(id=uuid.uuid1,email="Sam", password="123")
    create_user(test_user_2, get_session)
    test_user_3 = User(id=uuid.uuid1,email="Alice", password="123")
    create_user(test_user_3, get_session)
    test_admin_1 = Admin(id=uuid.uuid1,email="Jack", password="123")
    create_admin(test_admin_1, get_session)

    test_transaction_1=Transaction(id=uuid.uuid1, credits=12, date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)
    increase_user_balance(test_user_1, test_transaction_1, get_session)
    test_transaction_2=Transaction(id=uuid.uuid1, credits=5, date_time='17.01.2025', user_id=test_user_1.id, user=test_user_1)
    decrease_user_balance(test_user_1, test_transaction_2, get_session)
    test_transaction_3=Transaction(id=uuid.uuid1, credits=100, date_time='19.01.2025', user_id=test_user_1.id, user=test_user_1)
    decrease_user_balance(test_user_1, test_transaction_3, get_session)


    test_response_1 = Response(id=uuid.uuid1, response="some response", date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)
    create_response(test_response_1, get_session)
    test_request_1 = Request(id=uuid.uuid1, image=bytearray, date_time='12.01.2025', user_id=test_user_1.id, user=test_user_1)
    create_request(test_request_1, get_session)


    test_response_2 = Response(id=uuid.uuid1, response="some response", date_time='12.01.2025', user_id=test_user_2.id, user=test_user_2)
    create_response(test_response_2, get_session)
    test_request_2 = Request(id=uuid.uuid1, image=bytearray, date_time='12.01.2025', user_id=test_user_2.id, user=test_user_2)
    create_request(test_request_1, get_session)
    
    




