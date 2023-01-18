import os
from jwt import encode,decode
from dotenv import load_dotenv


load_dotenv()
skey = os.getenv("SECRET_KEY")

def create_token(data:dict):
    token: str = encode(payload=data,key=skey,algorithm="HS256")
    return token

def validate_token(token:str)-> dict:
    data: dict=decode(token,key=skey,algorithms=["HS256"])
    return data
