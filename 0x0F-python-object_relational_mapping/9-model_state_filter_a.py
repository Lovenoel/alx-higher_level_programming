#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
hbtn_0e_6_usa.
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
    states = session.query(
            State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Printing results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Clean-up
    session.close()
