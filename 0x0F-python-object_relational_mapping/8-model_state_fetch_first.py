#!/usr/bin/python3

'''
Script that prints the first State object from the database hbtn_0e_6_usa

The script should take 3 arguments: mysql username,
mysql password and database name
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:
                           {sys.argv[2]}@localhost:3306/{sys.argv[3]}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(state_id).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}.{state.name}")
