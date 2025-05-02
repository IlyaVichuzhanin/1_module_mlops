from fastapi import FastAPI
import uvicorn
from routes.home import home_router
from routes.user import user_router
from routes.balance import user_balance_router
from routes.ml import ml_router
from routes.price import price_router
from routes.transaction import user_transaction_router
from fastapi import FastAPI
import uvicorn
from database.database import init_db
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()


app.include_router(home_router)
app.include_router(user_router, prefix='/user')
app.include_router(user_balance_router, prefix='/balance')
app.include_router(price_router, prefix='/price')
app.include_router(ml_router, prefix='/ml')
app.include_router(user_transaction_router, prefix='/transactions')


origins=["*"]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()
         