from fastapi import APIRouter

event_router=APIRouter()

events=[]

@event_router.get("/")
async def get_events():
    """

    Эндпоинт для получения списка событий

    """

    return events

@event_router.post("/")
async def create_events(event: dict):
    """

    Эндпоинт для получения списка событий

    """
    events.append(event)
    return {"message": "Event created seccessfully", "event": event}

@event_router.get("/{event_id}")
async def get_event(event_id: int):
    """

    Эндпоинт для получения списка событий

    """
    event=next((event for event in events if even["id"]==event_id), None)
    if event is None:
        return {"message": "Event not found"}
    return event