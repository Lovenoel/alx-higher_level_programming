#!/usr/bin/python3
"""
Changes the name of a State object where id=2 to New Mexico in the database hbtn_0e_6_usa.
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
    state = session.query(State).filter_by(id=2).first()

    # Updating state name
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("Not found")

    # Clean-up
    session.close()
