from sqlalchemy import Column, Integer, String,ForeignKey,LargeBinary
from Categories.database import Base
from sqlalchemy.orm import Relationship


class Classical(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index= True)
    type = Column(String)
    name = Column(String)
    artist = Column(String)
    movie = Column(String)
    # file_id = Column(Integer, ForeignKey('files.id'))
    files = Relationship("Filetype", back_populates="songs")


class Pop(Base):
    __tablename__ ="pop_music"
    id = Column(Integer, primary_key=True, index= True)
    type = Column(String)
    name = Column(String)
    artist = Column(String)
    movie = Column(String)
    # file_id = Column(Integer, ForeignKey('files.id'))
    # files = Relationship("Filetype",back_populates="pop_music")


class Filetype(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index= True)
    file_name = Column(String)
    file_type = Column(String)
    file_content = Column(LargeBinary)
    song_id = Column(Integer, ForeignKey('songs.id'))
    songs = Relationship("Classical", back_populates="files")
    # pop_music = Relationship('Pop', back_populates= "files")
