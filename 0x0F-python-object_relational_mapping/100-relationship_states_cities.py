#!/usr/bin/python3
"""Script to create a State "California" with the City "San Francisco"."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State
    new_state = State(name="California")

    # Create a new City
    new_city = City(name="San Francisco", state=new_state)

    # Add new City to the State's cities relationship
    new_state.cities.append(new_city)

    # Add State and City to the session
    session.add(new_state)
    session.add(new_city)

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()
