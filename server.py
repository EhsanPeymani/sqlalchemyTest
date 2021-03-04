from models import *

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    print("Application started ...")

    path = "sqlite:///" + os.getcwd() + '/chinook.db'
    print("database address: ", path)
    engine = create_engine(path, echo=False)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    data = session.query(Employee).all()

    for emp in data:
        print(f"{emp.FirstName} {emp.LastName} @ {emp.BirthDate}")
    


if __name__ == "__main__":
    main()