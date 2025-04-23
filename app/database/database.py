from sqlmodel import SQLModel, Session, create_engine
from database.config import get_settings
from models.user import SignUpUser
from models.admin import Admin
from models.request import Request
from models.response import Response
import uuid

from services.crud.user import create_user, get_user_by_id
from services.crud.admin import create_admin
from services.crud.balance import increase_user_balance
from services.crud.balance import decrease_user_balance
from services.crud.request import create_request, get_request_by_id
from services.crud.response import create_response
from services.crud.price import set_price
from PIL import Image

engine = create_engine(url=get_settings().DATABASE_URL_psycopg, echo=True,pool_size=5, max_overflow=10)


def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        test_user_1_id=uuid.UUID("773e3742-c9ae-4f10-85d8-da3d0d3490b6")
        test_user_1 = SignUpUser(email="Bob", password="123", id=test_user_1_id)
        create_user(test_user_1,session)
        test_user_2_id=uuid.uuid4()
        test_user_2 = SignUpUser(email="Sam", password="123", id=test_user_2_id)
        create_user(test_user_2,session)
        test_user_3_id=uuid.uuid4()
        test_user_3 = SignUpUser(email="Alice", password="123", id=test_user_3_id)
        create_user(test_user_3,session)
        test_admin_id=uuid.uuid4()
        test_admin_1 = Admin(email="Jack", password="123",id=test_admin_id)
        create_admin(test_admin_1,session)
        set_price(10, session)

        increase_user_balance(test_user_1_id, 100, session)
        decrease_user_balance(test_user_1_id, session)
        increase_user_balance(test_user_2_id, 50, session)
        decrease_user_balance(test_user_2_id,session)

        # image = Image.new('RGB', (100, 200))
        # image_bytes = image.tobytes("hex", "rgb")
        # new_request=Request(image=image_bytes)
        # create_request(new_request,session)
        # request_from_db = get_request_by_id(1,session)
        # response1 = Response(response="some responce", user_id=user1.id, user=user1, request_id=request_from_db.id, request=request_from_db)
        # create_response(response1, session)

    

    




