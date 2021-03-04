from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer)
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

# CREATE TABLE "employees" 
# ( [EmployeeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
# [LastName] NVARCHAR(20) NOT NULL, 
# [FirstName] NVARCHAR(20) NOT NULL, 
# [Title] NVARCHAR(30), 
# [ReportsTo] INTEGER, 
# [BirthDate] DATETIME, 
# [HireDate] DATETIME, 
# [Address] NVARCHAR(70), 
# [City] NVARCHAR(40), 
# [State] NVARCHAR(40), 
# [Country] NVARCHAR(40), 
# [PostalCode] NVARCHAR(10), [Phone] NVARCHAR(24), [Fax] NVARCHAR(24), [Email] NVARCHAR(60), FOREIGN KEY ([ReportsTo]) REFERENCES "employees" ([EmployeeId]) ON DELETE NO ACTION ON UPDATE NO ACTION )

class Genre(Base):
    __tablename__ = "genres"
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)