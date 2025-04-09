from models.user import User
from typing import List, Optional



def get_all_users(session)->List[User]:
    return session.query(User).all()

def get_user_by_id(id:int, session) -> Optional[User]:
    user=session.get(User, id)
    if user:
        return user
    return None

def get_user_by_email(email:int, session) -> Optional[User]:
    user = session.query(User).filter(User.email==email).first()
    if user:
        return user
    return None


def create_user(new_user: User, session) -> None:
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

def delete_user_by_id(id:int, session) -> None:
    user = session.get(User, id)
    if user:
        session.delete[user]
        session.commit()
        return