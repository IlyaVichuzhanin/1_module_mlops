from models.balance import Balance
from typing import List, Optional



def get_all_balances(session)->List[Balance]:
    return session.query(Balance).all()

def get_balance_by_id(id:int, session) -> Optional[Balance]:
    balance=session.get(Balance, id)
    if balance:
        return balance
    return None

def get_balance_by_user(user_id:str, session) -> Optional[Balance]:
    balance = session.query(Balance).filter(Balance.user_id==user_id)
    if balance:
        return balance
    return None


def create_balance(new_balance: Balance, session) -> None:
    session.add(new_balance)
    session.commit()
    session.refresh(new_balance)

def delete_balance_by_id(id:int, session) -> None:
    balance = session.get(Balance, id)
    if balance:
        session.delete[balance]
        session.commit()
        return