import uuid
from models.user import User
from models.balance import Balance
from models.transaction import Transaction
from typing import List, Optional
from services.crud.transaction import create_transaction



def get_all_balances(session)->List[Balance]:
    return session.query(Balance).all()

def get_balance_by_id(id:uuid.UUID, session) -> Optional[Balance]:
    balance=session.get(Balance, id)
    if balance:
        return balance
    return None

def get_balance_by_user_id(user_id:uuid.UUID, session) -> Optional[Balance]:
    balance = session.query(Balance).filter(Balance.user_id==user_id)
    if balance:
        return balance
    return None

def increase_user_balance(user:User, transaction:Transaction, session) -> None:
    balance = session.query(Balance).filter(Balance.user_id==user.id)
    if balance:
        create_transaction(transaction, session)
        balance.current_balance += transaction.credits
        session.add(balance)
        session.refresh()
        session.commit()
        session.refresh(balance)
    return None


def decrease_user_balance(user:User, transaction:Transaction, session) -> None:
    balance = session.query(Balance).filter(Balance.user_id==user.id)
    if balance:
        if balance.current_balance>=transaction.credits:
            create_transaction(transaction, session)
            balance.current_balance -= transaction.credits
            session.add(balance)
            session.refresh()
            session.commit()
            session.refresh(balance)
        else:
            return "Недостаточно средств для списания"
    return None


def create_balance(new_balance: Balance, session) -> None:
    session.add(new_balance)
    session.commit()
    session.refresh(new_balance)

def delete_balance_by_id(id:uuid.UUID, session) -> None:
    balance = session.get(Balance, id)
    if balance:
        session.delete[balance]
        session.commit()
        return