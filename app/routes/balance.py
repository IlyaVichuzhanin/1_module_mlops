from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.balance import Balance
from services.crud import balance as BalanceService



user_balance_router = APIRouter()


@user_balance_router.get('/get_user_balance',  response_model=Balance)
async def get_user_balance(user_id: int, session=Depends(get_session))->Balance:
    user_balance = BalanceService.get_balance_by_user_id(user_id, session)
    return user_balance



@user_balance_router.put('/increase_user_balance')
async def increase_user_balance(user_id:int, credits: float, session=Depends(get_session))->None:
    BalanceService.increase_user_balance(user_id, credits, session)
    return {"message": "User balance has been increased!"}


@user_balance_router.put('/decrease_user_balance')
async def decrease_user_balance(user_id:int, session=Depends(get_session))->None:
    BalanceService.decrease_user_balance(user_id, session)
    return {"message": "User balance has been decreased!"}


