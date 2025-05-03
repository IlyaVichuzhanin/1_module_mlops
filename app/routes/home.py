from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from auth.hash_password import HashPassword
from database.config import get_settings
from auth.authanticate import authenticate_cookie
from services.crud import user as UserService
from database.database import get_session


settings=get_settings()
home_router=APIRouter(tags=['Home'])
hash_password=HashPassword()
templates = Jinja2Templates(directory="view")



@home_router.get("/", response_class=HTMLResponse)
async def index(request: Request, session=Depends(get_session)):
    token=request.cookies.get(settings.COOKIE_NAME)
    if token:
        user_email = await authenticate_cookie(token)
        if user_email:
            user = UserService.get_user_by_email(user_email,session)
            if(user):
                return templates.TemplateResponse("personal_cabinet.html", {"request": request})
    return templates.TemplateResponse("index.html", {"request": request})
            
 
    

    