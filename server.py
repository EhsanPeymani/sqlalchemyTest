from models import *
from dbFunctions import PrintEmployeeCustomers, PrintManagerEmployees

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    print("Application started ...")

    path = "sqlite:///" + os.getcwd() + '/chinook.db'
    print("database address: ", path)
    engine = create_engine(path, echo=False)
    session = Session(engine)

    PrintEmployeeCustomers(session, False)

    PrintManagerEmployees(session, False)

    track = Track(Name="MyTrack")
    playlist = Playlist(Name="NewPlaylist")
    playlist.Tracks.append(track)
    print(len(track.Playlists), " ", track.Playlists[0].Name)
    

    # print("------------------------------------")
    # data = session.query(Customer).all()
    # for cust in data:
    #     p = [str(invoice.InvoiceId) for invoice in cust.Invoices]
    #     print(f"Customer {cust.CustomerId}: Invoice Ids {p} -> Supporting employee: {cust.Employee.FirstName} + {cust.Employee.LastName}")

    # print("------------------------------------")
    # invoice = session.query(Invoice).filter_by(InvoiceId=10).first()
    # print(f"Invoice {invoice.InvoiceId} relates to Customer {invoice.Customer.LastName}")     

if __name__ == "__main__":
    main()

