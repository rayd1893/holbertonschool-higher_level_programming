#!/usr/bin/python3
'''Import SQLAlchemy'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Create table state from ORM'''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        '''Define Constructor'''
        self.id = id
        self.name = name
