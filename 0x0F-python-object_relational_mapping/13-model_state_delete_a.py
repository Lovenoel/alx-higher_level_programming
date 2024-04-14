#!/usr/bin/python3
"""
Deletes all State objects with names containing the letter a from the data
base hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session object creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query execution
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Deleting states
    for state in states:
        session.delete(state)
    session.commit()

    # Clean-up
    session.close()
