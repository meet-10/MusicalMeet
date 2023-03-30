from pydantic import BaseModel
from typing import List, Optional




class SongCategoryBase(BaseModel):
    type: str


class SongCategory(SongCategoryBase):
    id:int
    class Config():
        orm_mode = True


class FiletypeBase(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes
    song_id: int


class Filetype(FiletypeBase):
    id: int
    class Config():
        orm_mode = True


class SongBase(BaseModel):
    type_id: int
    name: str
    artist: str
    movie: str
   


class Song(SongBase):
    id: int
    
    class Config():
        orm_mode = True


class ShowSong(BaseModel):
    type_id : int
    name : str
    artist : str
    category : SongCategory
    audio : List[Song] =[]
    class Config():
        orm_mode = True
   


class ShowFile(BaseModel):
    song_id : int
    file_name: str
    file_type: str
    file_content: bytes
    files: ShowSong
    class Config():
        orm_mode = True


class ShowCategory(SongCategoryBase):
    id : int
    type : str
    songs : List[ShowSong]
    class Config():
        orm_mode = True
