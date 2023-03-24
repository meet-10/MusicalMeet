from sqlalchemy import Column, Integer, String,ForeignKey,LargeBinary
from Categories.database import Base
from sqlalchemy.orm import Relationship


class Classical(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String)
    artist = Column(String)
    movie = Column(String)
    file_id = Column(Integer, ForeignKey('files.id'))
    files = Relationship("Filetype", back_populates="songs")
   

class Filetype(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index= True)
    file_name = Column(String)
    file_type = Column(String)
    file_content = Column(LargeBinary)
    songs = Relationship("Classical", back_populates="files")