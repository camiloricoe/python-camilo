from fastapi import APIRouter
from fastapi import  Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()



@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db=Session()
    result=MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=10000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
            return JSONResponse(status_code=404, content={'message': 'Movie not found'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
# parametros Query ... clave y valor
@movie_router.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Movies in category not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
# def create_movie(movie: Movie): #funciona igual
def create_movie(movie: Movie) -> dict:
    db=Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

# put con el esquema
@movie_router.put('/movies/{id}', tags=['Movies'])
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
@movie_router.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
            return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': f'Se ha eliminado la pelicula con el id {id}'})
    
    