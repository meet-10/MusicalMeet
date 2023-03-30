from fastapi import APIRouter, Depends, status, HTTPException
from Categories import schemas, models
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from Categories.database import get_db


router = APIRouter(prefix="/songs", tags=["Songs"])

@router.get("/",response_model=List[schemas.ShowSong])
def all_songs(db:Session = Depends(get_db)):
    songs = db.query(models.Song).all()
    return songs


@router.post("/")
def create(song: schemas.Song, db: Session = Depends(get_db)):
    try:
        db_song = models.Song(name=song.name, artist=song.artist, movie=song.movie, type_id=song.type_id)
        db.add(db_song)
        db.commit()
        db.refresh(db_song)
        return db_song
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/{id}',status_code=200,response_model = schemas.ShowSong)
def show(id,db:Session = Depends(get_db)):
    
    db_song = db.query(models.Song).filter(models.Song.id == id).first()
    print(db_song)
    if not db_song:
        raise HTTPException(status_code=404,detail=f"id {id} not available")
    return db_song
