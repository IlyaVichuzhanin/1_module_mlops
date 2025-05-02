from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.transaction import Transaction
from services.crud import transaction as TransactionService
import uuid



user_transaction_router = APIRouter(tags=['Transactions'])


@user_transaction_router.get('/get_user_transactions/{user_id}',  response_model=list[Transaction])
async def get_user_transactions(user_id: str, session=Depends(get_session))->list[Transaction]:
    user_transactions = TransactionService.get_user_transactions(user_id, session)
    return user_transactions