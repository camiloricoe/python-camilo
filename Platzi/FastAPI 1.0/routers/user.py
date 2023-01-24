from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from jwt_manager import create_token
from fastapi import APIRouter

users_router = APIRouter()


class User(BaseModel):
    email:str = Field(default="correo@dominio.com")
    password:str = Field(default="1234")

@users_router.post('/login', tags=['Auth'])
def login(user: User):
    if user.email =="correo@dominio.com" and user.password =="1234":
        token: str = create_token(user.dict())
    return JSONResponse(content=token, status_code=200)