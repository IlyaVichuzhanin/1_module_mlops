from sqlmodel import Session, select
from sqlalchemy import desc
from typing import Optional
from models.price import Price
import uuid
    




def set_price(new_price: float, session: Session) -> None:
    price=Price(credits=new_price)
    session.add(price)
    session.commit()
    session.refresh(price)


def get_current_price(session:Session) -> Optional["Price"]:
    statement = select(Price).order_by(Price.date_time.desc())
    price = session.exec(statement).first()
    if price:
        return price
    return None








