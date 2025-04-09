from models.response import Response
from typing import List, Optional



def get_all_responses(session)->List[Response]:
    return session.query(Response).all()

def get_responce_by_id(id:int, session) -> Optional[Response]:
    responce=session.get(Response, id)
    if responce:
        return responce
    return None

def get_user_responses(user_id:int, session) -> Optional[List[Response]]:
    return session.query(Response).filter(Response.user_id==user_id).all()


def create_response(new_response: Response, session) -> None:
    session.add(new_response)
    session.commit()
    session.refresh(new_response)

def delete_response_by_id(id:int, session) -> None:
    response = session.get(Response, id)
    if response:
        session.delete[response]
        session.commit()
        return