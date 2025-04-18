from fastapi import FastAPI
import uvicorn
from routes.home import home_router
from routes.event import event_router
from routes.user import user_router
from routes.balance import user_balance_router
from routes.ml import ml_router
from fastapi import FastAPI
import uvicorn
from database.database import init_db





app=FastAPI()
app.include_router(home_router, tags=['home'])
app.include_router(event_router, prefix='/events', tags=['home'])
app.include_router(user_router)
app.include_router(user_balance_router)
app.include_router(ml_router)


if __name__=='__main__':
    print("1111111111111111112222222222222222222222222222222222222!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    uvicorn.run('api:app', host='0.0.0.0',port=8080, reload=True)
    init_db() 