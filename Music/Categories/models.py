from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from Categories.database import Base
from sqlalchemy.orm import Relationship


class SongCategory(Base):
    __tablename__ = "song_categories"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    songs = Relationship("Song", back_populates="category")
    
   


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("song_categories.id"))
    name = Column(String)
    artist = Column(String)
    movie = Column(String)
    category = Relationship("SongCategory", back_populates="songs")
    
    
    files = Relationship("Filetype", back_populates="audio")


class Filetype(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("songs.id"))
    file_name = Column(String)
    file_type = Column(String)
    file_content = Column(LargeBinary)

    audio = Relationship("Song", back_populates="files")
