from fastapi import FastAPI
import uvicorn
from routes.home import home_router
from routes.user import user_router
from routes.balance import user_balance_router
from routes.ml import ml_router
from routes.price import price_router
from fastapi import FastAPI
import uvicorn
from database.database import init_db


app=FastAPI()
init_db()

app.include_router(home_router)
app.include_router(user_router)
app.include_router(user_balance_router)
app.include_router(price_router)
app.include_router(ml_router)


if __name__=='__main__':
        uvicorn.run('api:app', host='0.0.0.0',port=8080, reload=True)
         