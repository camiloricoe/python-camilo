from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from jwt_manager import create_token
from config.database import  Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router


app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email:str = Field(default="correo@dominio.com")
    password:str = Field(default="1234")

@app.post('/login', tags=['Auth'])
def login(user: User):
    if user.email =="correo@dominio.com" and user.password =="1234":
        token: str = create_token(user.dict())
    return JSONResponse(content=token, status_code=200)

