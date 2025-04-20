from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from services.crud import user as UserService
from services.crud import request as RequestService
from services.crud import response as ResponseService
from typing import List
from py_linq import Enumerable
from models.user import SignInUser
from models.user import SignUpUser



user_router = APIRouter()


@user_router.post('/signup')
async def signup(data: "SignUpUser", session=Depends(get_session))->dict:
    if UserService.get_user_by_email(data.email, session) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with supplied username exists")
    UserService.create_user(data, session)
    return {"message": "User successfuly registred!"}


@user_router.post('/signin')
async def signin(data: "SignInUser", session=Depends(get_session))->dict:
    user = UserService.get_user_by_email(data.email, session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    
    if user.hashed_password!=UserService.get_hash_password(data.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials!")

    return {"message": "User signed is successful!"}

@user_router.get('/get_all_users',  response_model=List[User])
async def get_all_users(session=Depends(get_session))->List[User]:
    return UserService.get_all_users(session)


@user_router.get('/get_user_predictions/',  response_model=List[tuple])
async def get_user_predictions(user_id: int, session=Depends(get_session))->List[tuple]:
    return ResponseService.get_user_predictions(user_id, session)



