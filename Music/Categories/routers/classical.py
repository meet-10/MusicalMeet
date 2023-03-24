from fastapi import APIRouter,Depends,status,HTTPException
from Categories import schemas,models
from typing import List
from sqlalchemy.orm import Session
from Categories.database import get_db


router = APIRouter()



@router.get('/classical',response_model=List[schemas.Show_songs],tags=['Classical'])

def all_songs(db: Session = Depends(get_db)):
    songs = db.query(models.Classical).all()
    return songs

@router.post('/',status_code= status.HTTP_201_CREATED,tags=['Classical'])

async def create(songs:schemas.songs,db:Session = Depends(get_db)):
    # creating new Schema
    new_song = models.Classical(name = songs.name, artist = songs.artist,movie = songs.movie,file_id = 1)
    # Adding it to Db
    db.add(new_song)
    #  To execute it
    db.commit()
    db.refresh(new_song)

    return new_song

@router.get('/{id}',status_code=200,response_model = schemas.Show_songs,tags=['Classical'])
def show(id,db:Session = Depends(get_db)):
    
    songs = db.query(models.Classical).filter(models.Classical.id == id).first()
    if not songs:
        raise HTTPException(status_code=404,detail=f"id {id} not available")
    return songs