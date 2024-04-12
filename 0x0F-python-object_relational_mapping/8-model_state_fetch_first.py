#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session object creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query execution
    state = session.query(State).first()

    # Printing result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Clean-up
    session.close()
