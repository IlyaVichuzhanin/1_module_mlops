from fastapi import FastAPI
import uvicorn
from routes.home import home_router
from routes.event import event_router
from routes.user import user_router
from fastapi import FastAPI
import uvicorn
from database.database import init_db





app=FastAPI()
app.include_router(home_router, tags=['home'])
app.include_router(event_router, prefix='/events', tags=['home'])
app.include_router




if __name__=='__main__':
    uvicorn.run('api:app', host='0.0.0.0',port=8080, reload=True)
    init_db() 