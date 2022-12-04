#!/usr/bin/python3
"""
Defines the class City that inherits from Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    Inherits from Base and links to the MySQL table `cities`
    Attributes:
      id(int) : column of an auto-generated, unique integer, can’t be null
       and is a primary key
      name(str) : column of a string with maximum 128 characters
       and can’t be null
      state_id(int) : column of an integer, can’t be null and is a
       foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
