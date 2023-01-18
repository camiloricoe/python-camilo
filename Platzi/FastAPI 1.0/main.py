from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse



app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"

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

#metodo get

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1 style=color:red> Hola Mundo </h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


#parametro de ruta
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id']==id:
            return movie
    return []

#parametros Query ... clave y valor
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie['category'] == category]


#metodo post
@app.post('/movies', tags=['movies'])
def craete_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

#put 
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item['id']==id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies

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
