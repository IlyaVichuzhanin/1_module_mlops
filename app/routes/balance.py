from fastapi import APIRouter,  Depends, Request, Response, Form
from database.database import get_session
from models.balance import Balance
from services.crud import balance as BalanceService
import uuid
from fastapi import APIRouter, Depends,  Request
from database.database import get_session
from services.crud import user as UserService
from services.crud import transaction as TransactionService
from auth.hash_password import HashPassword
from fastapi.templating import Jinja2Templates
from database.config import get_settings
from auth.authanticate import authenticate_cookie



user_balance_router = APIRouter(tags=['Balance'])
hash_password = HashPassword() 
templates = Jinja2Templates(directory="view")
settings=get_settings()

@user_balance_router.get('/get_user_balance')
async def get_user_balance(request: Request, session=Depends(get_session)):
    token=request.cookies.get(settings.COOKIE_NAME)
    if token:
        user_email = await authenticate_cookie(token)
        if user_email:
            user = UserService.get_user_by_email(user_email,session)
            if(user):
                balance=BalanceService.get_balance_by_user_id(user.id, session)
                transactions = TransactionService.get_user_transactions(user.id, session)
                context={
                    "balance": balance.current_balance,
                    "transactions": transactions,
                    "request": request
                }
                return templates.TemplateResponse("balance.html", context) 
    
    return templates.TemplateResponse("signup.html", context)



@user_balance_router.post('/increase_user_balance')
async def increase_user_balance(request: Request, credits: str = Form(...), session=Depends(get_session)):
    token=request.cookies.get(settings.COOKIE_NAME)
    if token:
        user_email = await authenticate_cookie(token)
        if user_email:
            user = UserService.get_user_by_email(user_email,session)
            if(user):
                BalanceService.increase_user_balance(user.id, credits, session)
                transactions = TransactionService.get_user_transactions(user.id, session)
                balance=BalanceService.get_balance_by_user_id(user.id, session)
                context={
                    "balance": balance.current_balance,
                    "transactions": transactions,
                    "request": request
                }
                return templates.TemplateResponse("balance.html", context)
    return templates.TemplateResponse("signup.html", context)


@user_balance_router.put('/decrease_user_balance')
async def decrease_user_balance(user_id:int, session=Depends(get_session))->None:
    BalanceService.decrease_user_balance(uuid.UUID(user_id), session)
    return {"message": "User balance has been decreased!"}


