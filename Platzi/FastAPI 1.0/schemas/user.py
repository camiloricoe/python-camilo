from pydantic import BaseModel, Field


class User(BaseModel):
    email:str = Field(default="correo@dominio.com")
    password:str = Field(default="1234")