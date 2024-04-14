#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa grouped by state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Database connection
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session object creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query execution
    data = session.query(State, City).join(City).order_by(City.id).all()

    # Printing results
    for state, city in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Clean-up
    session.close()
