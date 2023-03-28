from fastapi import APIRouter,Depends,status,HTTPException
from Categories import schemas,models
from typing import List
from sqlalchemy.orm import Session
from Categories.database import get_db

router = APIRouter(
    prefix= "/pop",
    tags = ['Pop Music']
)


@router.get('/', response_model=List[schemas.Show_pop_music])
def all_songs(db: Session = Depends(get_db)):
    songs = db.query(models.Pop).all()
    return songs


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create(songs:schemas.Pop_music,db:Session = Depends(get_db)):
    
    new_song = models.Pop(name = songs.name,artist = songs.artist,movie = songs.movie,type = songs.type) #file_id = songs.file_id
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song


@router.get('/{id}',status_code=200,response_model= schemas.Show_pop_music)
def show(id,db:Session=Depends(get_db)):
    songs = db.query(models.Pop).filter(models.Pop.id == id).first()
    if not songs:
        raise HTTPException(status_code=404,detail=f"id {id} not available")
    return songs
    

