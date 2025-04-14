from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from models.balance import Balance
from models.transaction import Transaction
from services.crud import user as UserService
from services.crud import balance as BalanceService
from services.crud import response as ResponseService
from typing import List
from py_linq import Enumerable



user_balance_router = APIRouter()


@user_balance_router.get('/user_balance/{user_id}')
async def get_user_balance(user_id: int, session=Depends(get_session))->Balance:
    user_balance = BalanceService.get_balance_by_user_id(user_id, session)
    return user_balance



@user_balance_router.put('/user_balance/{user_id}/')
async def increase_user_balance(user_id:int, transaction: Transaction, session=Depends(get_session))->Balance:
    BalanceService.increase_user_balance(user_id, transaction, session)
    return {"message": "User balance has been increased!"}


