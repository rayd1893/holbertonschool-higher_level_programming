#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    citiesByStates = session.query(City) \
        .join(State, City.states) \
        .order_by(City.id) \
        .all()

    for city in citiesByStates:
        print(f'{city.states.name}: ({city.id}) {city.name}')
