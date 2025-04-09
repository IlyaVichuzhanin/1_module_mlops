from models.request import Request
from typing import List, Optional



def get_all_requests(session)->List[Request]:
    return session.query(Request).all()

def get_request_by_id(id:int, session) -> Optional[Request]:
    request=session.get(Request, id)
    if request:
        return request
    return None

def get_user_requests(user_id:int, session) -> Optional[List[Request]]:
    return session.query(Request).filter(Request.user_id==user_id).all()



def create_request(new_request: Request, session) -> None:
    session.add(new_request)
    session.commit()
    session.refresh(new_request)

def delete_request_by_id(id:int, session) -> None:
    request = session.get(Request, id)
    if request:
        session.delete[request]
        session.commit()
        return