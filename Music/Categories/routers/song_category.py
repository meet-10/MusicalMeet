from fastapi import APIRouter, Depends, status, HTTPException
from Categories import schemas, models
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from Categories.database import get_db


router = APIRouter(prefix="/song_category", tags=["Song Category"])


@router.get("/", response_model= List[schemas.ShowCategory])
def all_category(db: Session = Depends(get_db)):
    category = db.query(models.SongCategory).all()
    return category


# Route to create a new Song
@router.post("/")
def create(song_category: schemas.SongCategory, db: Session = Depends(get_db)):
    try:
        db_song_category = models.SongCategory(type=song_category.type)
        db.add(db_song_category)
        db.commit()
        db.refresh(db_song_category)
        return db_song_category                
    # {"id": db_song_category.id, "type": db_song_category.type}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get('/{id}',status_code=200,response_model = schemas.ShowCategory)
def show(id,db:Session = Depends(get_db)):
    
    db_type = db.query(models.SongCategory).filter(models.SongCategory.id == id).first()
    print(db_type)
    if not db_type:
        raise HTTPException(status_code=404,detail=f"id {id} not available")
    return db_type
