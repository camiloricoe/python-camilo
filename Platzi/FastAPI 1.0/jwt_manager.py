import os
from jwt import encode
from dotenv import load_dotenv


load_dotenv()
skey = os.getenv("SECRET_KEY")

def create_token(data:dict):
    token: str = encode(payload=data,key=skey,algorithm="HS256")
    return token
