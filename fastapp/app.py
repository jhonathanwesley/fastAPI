from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Primeiro endpoint com fastAPI'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def write_html():
    with open('fastapp/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HTMLResponse(html_content, HTTPStatus.OK)