from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from auth.hash_password import HashPassword
from database.config import get_settings


settings=get_settings()
home_router=APIRouter(tags=['Home'])
hash_password=HashPassword()
templates = Jinja2Templates(directory="view")



@home_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    

    