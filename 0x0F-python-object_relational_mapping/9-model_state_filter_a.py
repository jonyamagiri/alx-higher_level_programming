#!/usr/bin/python3
"""
return state objects containing letter 'a' from database via python
parameters given to script: username, password, database
"""

import sys
from model_state import Base, State
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

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
