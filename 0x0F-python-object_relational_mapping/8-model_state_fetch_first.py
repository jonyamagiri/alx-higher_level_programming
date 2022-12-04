#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Arguments: mysql username, mysql password and database name
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

    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{}: {}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()
