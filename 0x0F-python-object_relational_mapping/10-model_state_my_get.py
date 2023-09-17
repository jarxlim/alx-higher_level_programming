#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == name).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
