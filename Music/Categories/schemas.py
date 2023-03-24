from pydantic import BaseModel
from typing import List


class songs(BaseModel):
    name : str
    singer : str
    movie : str

class Show_songs(BaseModel):
    name :str
    singer : str
    movie :str
    class Config():
        orm_mode = True
