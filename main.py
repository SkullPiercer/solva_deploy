import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
def homepage(request: Request):
    return templates.TemplateResponse(
        "homepage.html",
        {
            "request": request,
            "title": "Главная страница",
            "notes": ["Первая", "Вторая", "Третья"]
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)