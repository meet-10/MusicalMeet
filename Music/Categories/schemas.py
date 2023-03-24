from pydantic import BaseModel
from typing import List

class SongBase(BaseModel):
    name : str
    artist : str
    movie : str
    file_id : int

class songs(SongBase):
    class Config():
        orm_mode = True

class File(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes

class Show_file(BaseModel):
    file_name : str
    file_type : str
    songs : List[songs]
    class Config():
        orm_mode = True

class Show_songs(BaseModel):
    name :str
    artist : str
    movie :str
    files : Show_file
    class Config():
        orm_mode = True






