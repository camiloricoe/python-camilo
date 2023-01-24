from fastapi import FastAPI, Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token
from config.database import Session, Base, engine
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"
app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email:str = Field(default="correo@dominio.com")
    password:str = Field(default="1234")

#esquemas con pydantic
class Movie(BaseModel):
    id: int | None = None
    #id: Optional[int]
    title: str = Field(default="Mi pelicula", min_length=1, max_length=25)
    overview: str = Field(max_length=120)
    year: int = Field(..., gt=1900, le=2022)
    rating: Optional[float] = Field(le=10.0)
    category: str

    class Config:
        schema_extra = {
            "example": {
                "title": "The Shawshank Redemption",
                "overview": "Two imprisoned",
                "year": 1994,
                "rating": 9.3,
                "category": "Drama",
            }
        }


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]


@app.post('/login', tags=['Auth'])
def login(user: User):
    if user.email =="correo@dominio.com" and user.password =="1234":
        token: str = create_token(user.dict())
    return JSONResponse(content=token, status_code=200)


@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db=Session()
    result=db.query(MovieModel).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@app.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=10000)) -> Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
            return JSONResponse(status_code=404, content={'message': 'Movie not found'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
# parametros Query ... clave y valor
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Movies in category not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
# def create_movie(movie: Movie): #funciona igual
def create_movie(movie: Movie) -> dict:
    db=Session()
    new_movie= MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

# put con el esquema
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
            return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    result.title=movie.title
    result.overview=movie.overview
    result.year =movie.year
    result.rating =movie.rating
    result.category =movie.category
    db.commit()
    return JSONResponse(status_code=200, content={'message': f'Se ha actualizado la pelicula con el id {id}'})

        
#delete
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
            return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': f'Se ha eliminado la pelicula con el id {id}'})
    
    