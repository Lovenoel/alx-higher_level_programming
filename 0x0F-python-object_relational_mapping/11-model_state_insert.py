#!/usr/bin/python3
"""
Adds the State object Louisiana to the database hbtn_0e_6_usa.
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

    # Creating a new State object
    new_state = State(name="Louisiana")

    # Adding the new state to the session
    session.add(new_state)

    # Committing changes to the database
    session.commit()

    # Printing the ID of the new state
    print(new_state.id)

    # Clean-up
    session.close()
