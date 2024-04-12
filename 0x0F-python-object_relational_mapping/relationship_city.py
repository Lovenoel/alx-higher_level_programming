#!/usr/bin/python3
"""Module for City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State

class City(Base):
    """City class to interact with the ORM."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        """Initializes a City instance."""
        self.name = name
