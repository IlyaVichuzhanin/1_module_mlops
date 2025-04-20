from fastapi import APIRouter, Body, HTTPException

home_router=APIRouter()

@home_router.get("/")
async def index()->dict:
    """

    Корневой эндпоинт, возвращающий приветсвенное сообщение

    """
    return {"message": "Hello world!!!"}