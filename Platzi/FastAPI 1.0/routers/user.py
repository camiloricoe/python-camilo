from fastapi.responses import JSONResponse
from jwt_manager import create_token
from fastapi import APIRouter
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['Auth'])
def login(user: User):
    if user.email =="correo@dominio.com" and user.password =="1234":
        token: str = create_token(user.dict())
    return JSONResponse(content=token, status_code=200)