from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.balance import Balance
from services.crud import price as PriceService



price_router = APIRouter()


@price_router.post('/set_price')
async def set_price(new_price:float, session=Depends(get_session))->None:
    PriceService.set_price(new_price, session)
    return {"message": "Price has been changed!"}