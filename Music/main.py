from fastapi import FastAPI,Request,Depends,status,HTTPException,File, UploadFile
from Categories import schemas,models
from Categories.database import get_db,engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from typing_extensions import Annotated
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind = engine)
templates = Jinja2Templates(directory="Templates")


@app.get('/',response_class=HTMLResponse,tags=['Music'])
def home(request : Request):

    data = {
            "Pop": "Pop Music",
            "alternate":"Alternate Music",
            "electronic":"Electronic Music",
            "jazz": "Jazz Music",
            "classical": "Classical Music"
            }

    return templates.TemplateResponse("page.html",{"request": request,"data": data})

@app.get('/classical',response_model=List[schemas.Show_songs],tags=['Classical'])

def all_songs(db: Session = Depends(get_db)):
    songs = db.query(models.Classical).all()
    return songs

@app.post('/',status_code= status.HTTP_201_CREATED,tags=['Classical'])

async def create(file: UploadFile,songs:schemas.songs,db:Session = Depends(get_db)):
    # creating new Schema
    
    new_song = models.Classical(name = songs.name, singer = songs.singer,movie = songs.movie,audio = songs.audio)
    # Adding it to Db
    db.add(new_song)
    #  To execute it
    db.commit()
    db.refresh(new_song)
    return new_song

@app.get('/{id}',status_code=200,response_model = schemas.Show_songs,tags=['Classical'])
def show(id,db:Session = Depends(get_db)):
    
    songs = db.query(models.Classical).filter(models.Classical.id == id).first()
    if not songs:
        raise HTTPException(status_code=404,detail=f"id {id} not available")
    return songs


@app.post("/uploadfile/",tags=['Classical'])
async def Upload_file(file: UploadFile,db:Session = Depends(get_db)):
   #data = file.file.read()
   return {"filename": file.filename, "type" : file.content_type}
