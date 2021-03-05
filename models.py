from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

playlist_track = Table(
    "playlist_track",
    Base.metadata,
    Column("PlaylistId", Integer, ForeignKey("playlists.PlaylistId")),
    Column("TrackId", Integer, ForeignKey("tracks.TrackId"))
)

class Employee(Base):
    __tablename__ = "employees"
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('employees.EmployeeId')) # self reference
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
    Customers = relationship("Customer", backref=backref("Employee"))
    Manager = relationship("Employee", remote_side=[EmployeeId])
    ReportingEmployees = relationship("Employee", backref=backref("ReportingManager", remote_side=[EmployeeId]))
    # Manager and ReportingManager will be the same thing

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
    tracks = relationship("Track", backref=backref("Genre"))

class MediaType(Base):
    __tablename__ = "media_types"
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String(120))
    tracks = relationship("Track", backref=backref("MediaType"))

class Track(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(120))
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer, ForeignKey("media_types.MediaTypeId"))
    GenreId = Column(Integer, ForeignKey("genres.GenreId"))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)
    Playlists = relationship("Playlist", secondary=playlist_track, back_populates="Tracks")
    

class Playlist(Base):
    __tablename__ = "playlists"
    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String(120))
    Tracks = relationship("Track", secondary=playlist_track, back_populates="Playlists")

