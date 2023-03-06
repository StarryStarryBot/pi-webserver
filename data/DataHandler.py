import csv
from pathlib import Path

from datetime import datetime

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

from helpers.QuadTree import Index

class StarData:
    def __init__(self):
        # list of all star objects
        self.db = None
        # quadtree of starobjects
        self.star_locations = None
        self.load_data()
        
    def load_data(self):
        path = Path(__file__).parent / "star-data.csv"
        with open(path, newline='') as reader:
            self.db = [{k: v for k, v in row.items()} for row in csv.DictReader(reader, skipinitialspace=True)]
    
    def find_star(self, attribute: "id", value):
        for star_data in self.db:
            if star_data [attribute] == value:
                star = Star(star_data)
                return star

# will store the star data: attribute
# will also include the converters that conver to earth location
class Star:
    def __init__(self, data):
        self.db = None
        self.data = data

        self.sky_coordinates = SkyCoord(ra = float(self.data["ra"]) * u.hours, dec = float(self.data["dec"]) * u.degree) 
    
    def update_location(self):
        # location of USC
        self.user_location = EarthLocation(lat=34.02*u.deg, lon=-118.29*u.deg, height=54*u.m)

    def get_sky_coordinates(self):
        self.update_location()
        
        current_time = Time(datetime.now())
        return self.sky_coordinates.transform_to(AltAz(obstime = current_time, location = self.user_location))

