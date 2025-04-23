
from sqlmodel import Session
import bcrypt
from typing import TYPE_CHECKING,List, Optional
from models.balance import Balance
from services.crud.balance import create_balance
from models.user import User
import uuid
if TYPE_CHECKING:
    from models.user import SignUpUser
       
    

def get_all_users(session)->List["User"]:
    return session.query(User).all()

def get_user_by_id(id:uuid.UUID, session:Session) -> Optional["User"]:
    user=session.get(User, id)
    if user:
        return user
    return None

def get_user_by_email(email:str, session:Session) -> Optional["User"]:
    user = session.query(User).filter(User.email==email).first()
    if user:
        return user
    return None


def create_user(create_user: "SignUpUser", session: Session) -> None:
    password_bytes = bytes(create_user.password, 'utf-8')
    new_user=User(email=create_user.email, hashed_password=get_hash_password(password_bytes), id=create_user.id)
    balance = Balance(user=new_user)
    create_balance(balance,session)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)


def delete_user_by_id(id:uuid.UUID, session:Session) -> None:
    user = session.get(User, id)
    if user:
        session.delete[user]
        session.commit()
        return

def get_hash_password(password:str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
    
