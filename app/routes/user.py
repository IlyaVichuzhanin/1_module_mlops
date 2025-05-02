from fastapi import APIRouter, Body, HTTPException, status, Depends, Response, Request, Form
from fastapi.security import OAuth2PasswordRequestForm
from database.database import get_session
from models.user import User, SignUpUser
from services.crud import user as UserService
from services.crud import request as RequestService
from services.crud import response as ResponseService
from typing import List
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from forms.usersignupform import UserSignUpForm
from forms.usersigninform import UserSignInForm
from fastapi.templating import Jinja2Templates
from database.config import get_settings
from fastapi.responses import RedirectResponse, PlainTextResponse



user_router = APIRouter(tags=['User'])
hash_password = HashPassword() 
templates = Jinja2Templates(directory="view")
settings=get_settings()

@user_router.post('/signin')
def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@user_router.post('/signup')
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request}) 

@user_router.post('/personal_account')
def get_personal_account(request: Request):
    return templates.TemplateResponse("personal_cabinet.html", {"request": request}) 
    
 


@user_router.post('/register')
async def register(request: Request, email: str = Form(...), password: str = Form(...), session=Depends(get_session)):
    form = UserSignUpForm(request)
    await form.load_data()
    user_exist=UserService.get_user_by_email(email, session)    
    
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with supplied username exists")
    
    if await form.is_valid():
        user_exist=UserService.get_user_by_email(email, session)
        if user_exist is None:
            hashed_password=hash_password.create_hash(password)
            new_user=User(email=email, hashed_password=hashed_password)
            UserService.create_user(new_user, session)
    else:
        print("Error Form")
 
    return templates.TemplateResponse("signin.html", {"request": request})


@user_router.post('/login')
async def login(response: Response, email: str = Form(...), password: str = Form(...), session=Depends(get_session)):

    user_exist=UserService.get_user_by_email(email, session)

    if user_exist is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    if hash_password.verify_hash(password, user_exist.hashed_password):
        access_token=create_access_token(user_exist.email)
        response.set_cookie(key=settings.COOKIE_NAME, value=access_token, httponly=True, expires=360000)
        return RedirectResponse("/user/personal_account")





@user_router.get('/get_all_users',  response_model=List[User])
async def get_all_users(session=Depends(get_session))->List[User]:
    return UserService.get_all_users(session)


@user_router.get('/get_user_predictions/',  response_model=List[tuple])
async def get_user_predictions(user_id: int, session=Depends(get_session))->List[tuple]:
    return ResponseService.get_user_predictions(user_id, session)



