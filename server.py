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

    print("Employee Reporters: ")
    for emp in data:
        print(f"{emp.FirstName} {emp.LastName} has {len(emp.Customers)} customers.")
    
    print("------------------------------------")
    data = session.query(Customer).all()
    for cust in data:
        p = [str(invoice.InvoiceId) for invoice in cust.Invoices]
        print(f"Customer {cust.CustomerId}: Invoice Ids {p}")

    print("------------------------------------")
    invoice = session.query(Invoice).filter_by(InvoiceId=10).first()
    print(f"Invoice {invoice.InvoiceId} relates to Customer {invoice.Customer.LastName}")     

if __name__ == "__main__":
    main()

