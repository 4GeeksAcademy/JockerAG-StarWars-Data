import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(16), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(50))

class Posts(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2000), nullable=False)
    img_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users')

    def to_dict(self):
        return {}
class Planets(Base):
    __tablename__ = 'planets'
    id= Column(Integer, primary_key=True)
    name = Column(String)

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')

class Films(Base):
    __tablename__= 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    year = Column(DateTime)

class CharacterFilms(Base):
    __tablename__ = 'character_films'
    id = Column(Integer, primary_key=True)
    character_id= Column(Integer, ForeignKey('characters.id'))
    film_id = Column(Integer, ForeignKey('films.id'))
    character = relationship('Characters', foreign_keys=['character_id']) 
    film = relationship('Films', foreign_keys=['film_id'])
    minutes = Column(DateTime)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
