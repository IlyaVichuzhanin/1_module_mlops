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
from services.crud.balance import create_balance

engine = create_engine(url=get_settings().DATABASE_URL_psycopg, echo=True,pool_size=5, max_overflow=10)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    test_user_1 = User(id=1,user_name="Bob", password="123")
    create_user(test_user_1)
    test_user_2 = User(id=2,user_name="Sam", password="123")
    create_user(test_user_2)
    test_user_3 = User(id=3,user_name="Alice", password="123")
    create_user(test_user_3)
    test_admin_1 = Admin(id=1,user_name="Jack", password="123")
    create_admin(test_admin_1)
    test_transaction_1=Transaction(id=1, credits=12, date_time='12.01.2025', user_id=1, user=test_user_1)
    create_transaction(test_transaction_1)
    test_response_1 = Response(id=1, response="some response", date_time='12.01.2025', user_id=1, user=test_user_1)
    create_response(test_response_1)
    test_request_1 = Request(id=1, image=bytearray, date_time='12.01.2025', user_id=1, user=test_user_1)
    create_request(test_request_1)
    test_balance_1 = Balance(id=1, current_balance=15, user_id=1, user=test_user_1)
    create_balance(test_balance_1)
    




