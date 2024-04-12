#!/usr/bin/python3
"""Script that lists all City objects."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def main():
    """Main function."""
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        return

    username, password, database_name = sys.argv[1:]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    # Create metadata
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and corresponding states
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    main()
