from fastapi import FastAPI, HTTPException, Request
import uvicorn
from routes.home import home_router
from routes.event import event_router

app=FastAPI()
app.include_router(home_router, tags=['home'])
app.include_router(event_router, prefix='/events', tags=['home'])




if __name__=='__main__':
    uvicorn.run('api:app', host='0.0.0.0',port=8080, reload=True) 