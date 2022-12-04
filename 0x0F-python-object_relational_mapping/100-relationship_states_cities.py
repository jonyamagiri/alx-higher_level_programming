#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” from
 the database hbtn_0e_100_usa
Arguments: mysql username, mysql password and database name
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
