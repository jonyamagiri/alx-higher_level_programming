#!/usr/bin/python3
"""
Defines the class State and has an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Inherits from Base and links to the MySQL table 'states'
    Attributes:
      id(int) : column of an auto-generated, unique integer, can’t be null
       and is a primary key
      name(str) : column of a string with maximum 128 characters
       and can’t be null
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
