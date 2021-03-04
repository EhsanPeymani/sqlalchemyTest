from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('employee.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    Customers = relationship("Customer", backref=backref("employees"))
    # Reporters = relationship("Employee", backref=backref("employees"))

class Customer(Base):
    __tablename__ = "customers"
    CustomerId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer, ForeignKey("employees.EmployeeId"))
    Invoices = relationship("Invoice", backref=backref("Customer"))

class Invoice(Base):
    __tablename__ = "invoices"
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey("customers.CustomerId"))
    InvoiceDate = Column(DateTime)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String(10))
    Total = Column(Float)



class Genre(Base):
    __tablename__ = "genres"
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)