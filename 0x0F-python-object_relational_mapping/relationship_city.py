#!/usr/bin/python3
"""The City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """The class City"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
