#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
Arguments: mysql username, mysql password and database name
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(
        State, City).filter(
        State.id == City.state_id).all()
    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
