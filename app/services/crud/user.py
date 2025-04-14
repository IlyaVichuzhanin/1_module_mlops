import uuid
from models.user import User
from models.balance import Balance
from services.crud.balance import create_balance, get_balance_by_user_id
from typing import List, Optional



def get_all_users(session)->List[User]:
    return session.query(User).all()

def get_user_by_id(id:uuid.UUID, session) -> Optional[User]:
    user=session.get(User, id)
    if user:
        return user
    return None

def get_user_by_email(email:str, session) -> Optional[User]:
    user = session.query(User).filter(User.email==email).first()
    if user:
        return user
    return None


def create_user(new_user: User, session) -> None:
    new_balance = Balance(id=uuid.uuid1, current_balance=0, user_id=new_user.id, user=new_user)
    create_balance(new_balance)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

def delete_user_by_id(id:uuid.UUID, session) -> None:
    user = session.get(User, id)
    balance = get_balance_by_user_id(user_id=user.id)
    if user:
        session.delete[user]
        if balance:
            session.delete[balance]
            session.commit()
    return