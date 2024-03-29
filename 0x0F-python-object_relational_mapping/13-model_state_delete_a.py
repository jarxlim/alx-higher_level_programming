#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database
"""

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    delet = session.query(State).order_by(State.id).all()
    for row in delet:
        if 'a' in row.name:
            session.delete(row)
    session.commit()

    session.close()
