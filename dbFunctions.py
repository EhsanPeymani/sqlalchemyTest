from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql import asc, desc, func
from models import *

class Functions:
    def __init__(self, session):
        self.session = session

    def PrintEmployeeCustomers(self, doIt=False):
        if (not doIt):
            return
        employees = self.session.query(Employee).all()

        for emp in employees:
            if len(emp.Customers) > 0:
                emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName}"
                print(f"{emp_name}:")
                for cust in emp.Customers:
                    cust_name = "".ljust(10) + f"{cust.FirstName} {cust.LastName}"
                    print(cust_name)

    def PrintManagerEmployees(self, doIt=False):
        if (not doIt):
            return;

        employees = self.session.query(Employee).all()
        for emp in employees:
            emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName} ({len(emp.ReportingEmployees)})"
            emp_name_reports_to = emp_name.ljust(30) + "reports to "
            if emp.Manager is not None:
                print(emp_name_reports_to + f"{emp.Manager.FirstName} {emp.Manager.LastName} ({len(emp.Manager.ReportingEmployees)}) -> {emp.ReportingManager.LastName}")
            else:
                print(emp_name)

    def PrintCustomerSupports(self, doIt=False):
        if (not doIt):
            return

        customers = self.session.query(Customer).all()
        for customer in customers:
            print(f"{customer.FirstName} {customer.LastName}".ljust(30), f"{len(customer.Invoices)}".ljust(5), "<--", 
                f"{customer.SupportEmployee.FirstName} {customer.SupportEmployee.LastName}")

    def PrintArtistAlbumCount(self, doIt=False):
        if (not doIt):
            return
        
        artist_albums = (
            self.session.query(Artist.ArtistId, 
                               Artist.Name, 
                               func.count(Album.AlbumId).label("TotalAlbums")
                               )                               
                        .join(Album)
                        .group_by(Artist.ArtistId)
                        .order_by(desc("TotalAlbums"))
        )

        for rec in artist_albums:
            print(f"{str(rec.ArtistId).ljust(4)} ({str(rec.TotalAlbums).ljust(2)}) {rec.Name}: ")

    def PrintArtistTrackCount(self, doIt=False):
        if (not doIt):
            return
        
        artist_track = (
            self.session.query(func.count(Track.TrackId).label("total_tracks"), Artist.ArtistId, Artist.Name
            )
            .outerjoin(Album, Album.ArtistId == Artist.ArtistId)
            .outerjoin(Track, Track.AlbumId == Album.AlbumId)
            .group_by(Artist.ArtistId)
            .order_by(desc("total_tracks"))
        )

        for art in artist_track:
            print(f"{str(art.ArtistId).ljust(4)} {str(art.Name).ljust(100)}: {art.total_tracks}")

    def AddAlbum(self, album_title, artist_name, doIt=False):
        if (not doIt):
            return
        
        album = (
            self.session.query(Album)
                        .join(Artist)
                        .filter(
                            and_(Album.Title==album_title, Artist.Name==artist_name)
                        ).one_or_none()
        )

        if album is not None:
            print("Album exists")
            return
        else:
            album = Album(Title=album_title)
            print(f"{album_title} will be added to Album table")

        
        artist = (
            self.session.query(Artist)
                        .filter(Artist.Name==artist_name).one_or_none()
        )

        if artist is None:
            artist = Artist(Name=artist_name)
            print(f"{artist_name} added to Artist table")
            # self.session.add(artist)   # not needed since it will be added as album
        
        album.Artist = artist
        self.session.add(album)
        self.session.commit()
        


    
