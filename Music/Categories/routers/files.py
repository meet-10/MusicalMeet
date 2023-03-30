from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
    File,
    UploadFile,
    Response,
)
from Categories import schemas, models
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from Categories.database import get_db


router = APIRouter(prefix="/files", tags=["Files"])


@router.get("/", response_model= List[schemas.ShowFile])
def all_files(db:Session = Depends(get_db)):
    files = db.query(models.Filetype).all()
    return files
    
@router.post("/uploadfile/")
async def Upload_file(
    song_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    try:
        # Read the contents of the uploaded file
        file_content = file.file.read()

        db_file = models.Filetype(
            file_name=file.filename,
            file_type=file.content_type,
            file_content=file_content,
            song_id=song_id
        )

        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        return {
            "id": db_file.id,
            "file_name": db_file.file_name,
            "file_type": db_file.file_type,
            "song_id": db_file.song_id,
        }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    
@router.get("/{file_id}",response_model=schemas.ShowFile)
def read_file(file_id: int,db: Session = Depends(get_db)):
    db_file = db.query(models.Filetype).filter(models.Filetype.id == file_id).first()
    if not db_file:
        raise HTTPException(status_code=404,detail=f"id {file_id} not available")
    return Response(content=db_file.file_content, media_type=db_file.file_type)
