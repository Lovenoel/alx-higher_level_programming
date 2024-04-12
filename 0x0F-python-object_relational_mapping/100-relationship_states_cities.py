#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create California state
    california = State(name="California")
    session.add(california)
    session.commit()

    # Create San Francisco city linked to California
    san_francisco = City(name="San Francisco")
    san_francisco.state = california
    session.add(san_francisco)
    session.commit()


if __name__ == "__main__":
    main()
