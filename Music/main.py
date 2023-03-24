from fastapi import FastAPI,Request,Depends,status,HTTPException,File, UploadFile,Response
from Categories import schemas,models
from Categories.database import get_db,engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from typing_extensions import Annotated
from sqlalchemy.orm import Session
from Categories.routers import classical


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.include_router(classical.router)
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


@app.post("/uploadfile/",tags=['Files'])
async def Upload_file(file: UploadFile = File(...),db:Session = Depends(get_db)):
   new_file = models.Filetype(file_name = file.filename, file_type = file.content_type, file_content = file.file.read())
   db.add(new_file)
   db.commit()
   db.refresh(new_file)
   return {"file_id": new_file.id}

@app.get("/files/{file_id}",response_model=schemas.Show_file,tags=['Files'])
def read_file(file_id: int,db: Session = Depends(get_db)):
    db_file = db.query(models.Filetype).filter(models.Filetype.id == file_id).first()
    if not db_file:
        raise HTTPException(status_code=404,detail=f"id {file_id} not available")
    return Response(content=db_file.file_content, media_type=db_file.file_type)



