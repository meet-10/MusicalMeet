from sqlalchemy import Column, Integer, String,ForeignKey
from Categories.database import Base


class Classical(Base):

    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    singer = Column(String)
    movie = Column(String)