from models.user import User
from fastapi import FastAPI
import uvicorn


app=FastAPI()

@app.get('/')

def index():
    user_nick = User("123", "123", "123")
    return "Hello world!" + str(user_nick)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)





