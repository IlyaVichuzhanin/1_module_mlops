import uuid
from models.transaction import Transaction
from typing import List, Optional



def get_all_transactions(session)->List[Transaction]:
    return session.query(Transaction).all()

def get_transaction_by_id(id:int, session) -> Optional[Transaction]:
    transaction=session.get(Transaction, id)
    if transaction:
        return transaction
    return None

def get_user_transactions(user_id:uuid.UUID, session) -> Optional[List[Transaction]]:
    return session.query(Transaction).filter(Transaction.user_id==user_id).all()


def create_transaction(new_transaction: Transaction, session) -> None:
    session.add(new_transaction)
    session.commit()
    session.refresh(new_transaction)

def delete_transaction_by_id(id:uuid.UUID, session) -> None:
    transaction = session.get(Transaction, id)
    if transaction:
        session.delete[transaction]
        session.commit()
        return