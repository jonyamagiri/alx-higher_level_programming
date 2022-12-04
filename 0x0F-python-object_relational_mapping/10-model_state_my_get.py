#!/usr/bin/python3
"""
Prints the State object passed as argument from the database hbtn_0e_6_usa
Arguments: mysql username, mysql password, database name and
 state name to search (SQL injection free)
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
