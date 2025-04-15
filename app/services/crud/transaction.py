from models.transaction import Transaction
from models.user import User
from typing import List, Optional
from datetime import datetime
from services.crud.balance import decrease_user_balance



def get_all_transactions(session)->List[Transaction]:
    return session.query(Transaction).all()

def get_transaction_by_id(id:int, session) -> Optional[Transaction]:
    transaction=session.get(Transaction, id)
    if transaction:
        return transaction
    return None

def get_user_transactions(user_id:int, session) -> Optional[List[Transaction]]:
    return session.query(Transaction).filter(Transaction.user_id==user_id).all()


def create_transaction(new_transaction: Transaction, session) -> None:
    session.add(new_transaction)
    session.commit()
    session.refresh(new_transaction)

def delete_transaction_by_id(id:int, session) -> None:
    transaction = session.get(Transaction, id)
    if transaction:
        session.delete[transaction]
        session.commit()
        return
    
def provide_transaction(user:User, session)-> None:
    new_transaction=Transaction(
      credits=5,
      date_time=datetime.now(),
      user_id=user.id)
    create_transaction(new_transaction, session)
    decrease_user_balance(user_id=user.id,transaction=new_transaction,session=session)

    