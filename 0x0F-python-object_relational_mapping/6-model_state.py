#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if the state exists
    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state:
        cities = session.query(State, City).join(City).filter(State.name == sys.argv[4]).all()
        for city in cities:
            print(city[1].name)
    else:
        print("")

    # Close the session
    session.close()
