import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5,6]


@app.get('/contact')
def get_list():
    return {'name': "Camilo"}


@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola soy una página desde Python</h1>
    <p>y yo un párrafo</p>
    
    
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()
