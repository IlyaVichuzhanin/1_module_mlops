from sqlmodel import Session, select
from typing import TYPE_CHECKING, Optional, List
from models.user import User
from services.crud.price import get_current_price
from models.balance import Balance
from models.transaction import Transaction
from services.crud.transaction import create_transaction
    


def get_all_balances(session)->List["Balance"]:
    return session.query(Balance).all()

def get_balance_by_id(id:int, session:Session) -> Optional["Balance"]:
    balance=session.get(Balance, id)
    if balance:
        return balance
    return None

def get_balance_by_user_id(user_id:int, session:Session) -> Optional["Balance"]:
    statement = select(Balance).join(User).filter(User.id==user_id)
    balance = session.exec(statement).first()
    if balance:
        return balance
    return None

def increase_user_balance(user_id:int, credits:float, session:Session) -> None:
    balance = session.query(Balance).join(User).where(User.id==user_id).first()
    new_transaction = Transaction(credits=credits, user_id=user_id)
    if isinstance(balance,Balance):
        create_transaction(new_transaction, session)
        balance.current_balance += new_transaction.credits
        session.add(balance)
        session.commit()
        session.refresh(balance)
    return None


def decrease_user_balance(user_id:int, session:Session) -> None | str:
    balance = session.query(Balance).join(User).where(User.id==user_id).first()
    current_price = get_current_price(session)
    new_transaction = Transaction(credits=current_price.credits, user_id=user_id)
    if isinstance(balance,Balance):
        if balance.current_balance>=current_price.credits:
            create_transaction(new_transaction, session)
            balance.current_balance -= current_price.credits
            session.add(balance)
            session.commit()            
            session.refresh(balance)
        else:
            return "Недостаточно средств для списания"
    else:
        return "Баланс пользователя не найден!"
    return None


def create_balance(new_balance: "Balance", session: Session) -> None:
    session.add(new_balance)
    session.commit()
    session.refresh(new_balance)

def delete_balance_by_id(id:int, session) -> None:
    balance = session.get(Balance, id)
    if balance:
        session.delete[balance]
        session.commit()
        return