#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    newTable = session.query(City, State)\
                       .filter(City.state_id == State.id)\
                       .order_by(City.id.asc()).all()

    for cities, states in newTable:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
