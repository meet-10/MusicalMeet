from fastapi import FastAPI, Request, Response
from Categories import schemas, models
from Categories.database import engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Categories.routers import song_category, songs, files
from fastapi.staticfiles import StaticFiles


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(song_category.router)
app.include_router(songs.router)
app.include_router(files.router)


templates = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse, tags=["Music"])
def home(request: Request):
    data = {
        "Pop": "Pop Music",
        "alternate": "Alternate Music",
        "electronic": "Electronic Music",
        "jazz": "Jazz Music",
        "classical": "Classical Music",
    }

    return templates.TemplateResponse("page.html", {"request": request, "data": data})



