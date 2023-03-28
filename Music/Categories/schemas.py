from pydantic import BaseModel
from typing import List


class SongBase(BaseModel):
    name : str
    artist : str
    movie : str
    type : str
    # file_id : str



class songs(SongBase):
    class Config():
        orm_mode = True


class Pop_Music_Base(BaseModel):
    name : str
    artist : str
    movie : str
    # file_id : int
    type : str


class Pop_music(Pop_Music_Base):
    class Config():
        orm_mode = True

class File(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes
    song_id : int


class Show_file(BaseModel):
    file_name : str
    file_type : str
    class Config():
        orm_mode = True
        use_enum_values = True

class Show_songs(BaseModel):
    name :str
    artist : str
    movie :str
    type :str
    files : Show_file
    class Config():
        orm_mode = True


class Show_pop_music(BaseModel):
    name : str
    artist :str
    movie :str
    # files : Show_file
    class Config():
        orm_mode = True
    









