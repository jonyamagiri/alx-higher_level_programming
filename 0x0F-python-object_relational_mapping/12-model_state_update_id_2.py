#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
Arguments: mysql username, mysql password and database name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_update = session.query(State).filter(State.id == 2).first()

    if state_update:
        state_update.name = 'New Mexico'
        session.commit()

    session.close()
