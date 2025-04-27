from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from auth.authanticate import authenticate_cookie, authenticate
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.database import get_session
#from services.auth.loginform import LoginForm
from services.crud import user as UsersService
from database.config import get_settings
from typing import Dict


settings=get_settings()
home_router=APIRouter()
hash_password=HashPassword()
templates = Jinja2Templates(directory="view")





@home_router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    # token=request.cookies.get(settings.COOKIE_NAME)
    # user = await authenticate_cookie(token)
    # if user is None:
    #     user=None
    # context={
    #      "user": None,
    #      "request": request
    # }
    # if token:
    #     user = await authenticate_cookie(token)
    #     print(user)
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #     if user:
    #        return templates.TemplateResponse("signup.html", context) 
    # else:
    #     return templates.TemplateResponse("signup.html", context)
    
    return templates.TemplateResponse("index.html", {"request": request})
    

    