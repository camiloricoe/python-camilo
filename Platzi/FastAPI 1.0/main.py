from fastapi import FastAPI
from config.database import  Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import users_router


app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(users_router)

Base.metadata.create_all(bind=engine)



