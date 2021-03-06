from models import *
from dbFunctions import Functions

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    print("Application started ...")

    path = "sqlite:///" + os.getcwd() + '/chinook.db'
    print("database address: ", path)
    engine = create_engine(path, echo=True)
    session = Session(engine)
    functions = Functions(session)

    functions.PrintEmployeeCustomers()

    functions.PrintManagerEmployees()

    functions.PrintCustomerSupports()

    functions.PrintArtistAlbumCount()

    functions.AddAlbum("Big Ones", "Aerosmith")
    functions.AddAlbum("Shaylin Album 3", "Shaylin")

    functions.PrintArtistTrackCount(True)

if __name__ == "__main__":
    main()

