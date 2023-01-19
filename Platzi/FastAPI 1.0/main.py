from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth= await super().__call__(request)
        data= validate_token(auth.credentials)
        if data['email']!= "correo@dominio.com":
            raise HTTPException(status_code=403, detail="invalid Credemtials")
    

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
                "id": 9999,
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




#metodo get

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1 style=color:red> Hola Mundo </h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


#parametro de ruta
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int =Path(ge=1,le=10000)):
    for movie in movies:
        if movie['id']==id:
            return movie
    return []

#parametros Query ... clave y valor
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str =Query(min_length=5, max_length=15)):
    return [movie for movie in movies if movie['category'] == category]


# #metodo post
# @app.post('/movies', tags=['movies'])
# def craete_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
#     movies.append({
#         'id': id,
#         'title': title,
#         'overview': overview,
#         'year': year,
#         'rating': rating,
#         'category': category
#     })
#     return movies


# metodo post con el esquema
@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

# # put
# @app.put('/movies/{id}', tags=['movies'])
# def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     for item in movies:
#         if item['id'] == id:
#             item['title'] = title
#             item['overview'] = overview
#             item['year'] = year
#             item['rating'] = rating
#             item['category'] = category
#             return movies


# put con el esquema
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id']==id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies
        
# #Otra forma de hacer el update
# @app.put('/movies/{id}', tags=['movies'])
# async def update_movie(id: int, movie: Movie):

#     for index, item in enumerate(movies):
#         if item["id"] == id:
#             movies[index].update(movie)
#             movies[index]["id"] = id
#             return movies[index]

#delete
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int):
    for movie in movies:
        if movie['id']==id:
            movies.remove(movie)
            return movies

# #put
# @app.put('/movies/{id}', tags=['movies'])
# async def update_movie(id: int, request: Request):
#     update_movie = await request.json()
#     for index, item in enumerate(movies):
#         if item["id"] == id:
#             movies[index].update(update_movie)
#             return movies[index]

#     raise HTTPException(status_code=404, detail="Movie not found")

# #delete
# @app.delete('/movies/{id}', tags=['movies'])
# async def delete_movie(id: int):
#     for index, item in enumerate(movies):
#         if item["id"] == id:
#             del movies[index]
#             return {'status': 'deleted movie'}

#     raise HTTPException(status_code=404, detail="Movie not found")



# JSONResponse

@app.get('/moviesJSON', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies2() -> List[Movie]:
    return JSONResponse(status_code=200,content=movies )


@app.get('/moviesJSON/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie2(id: int = Path(ge=1, le=10000)) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404, content=[])

# parametros Query ... clave y valor
@app.get('/moviesJSON/', tags=['movies'])
def get_movies_by_category2(category: str = Query(min_length=5, max_length=15),status_code = 200):
    data = [movie for movie in movies if movie['category'] == category]
    return JSONResponse(status_code=200, content=data)


@app.post('/moviesJSON', tags=['movies'], response_model=dict, status_code=201)
# def create_movie(movie: Movie): #funciona igual
def create_movie2(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})
