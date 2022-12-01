import csv
from distutils.command.sdist import sdist
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

class StarData:
    def __init__(self):
        self.db = None
        self.load_db()
        
    def load_db(self):
        with open('star-data.csv', newline='') as reader:
            self.db = [{k: v for k, v in row.items()} for row in csv.DictReader(reader, skipinitialspace=True)]
    
    def find_star(self, attribute: "id", value):
        for star in self.db:
            if star[attribute] == value:
                return star
    
    # def find_closest_match(ra, dec):
    #     int closest_value = 1000

# will store the star data: attribute
# will also include the converters that conver to earth location
class Star:
    def __init__(self):
        self.db = None

# will store a list of stars
# stardata will include find constellation
class Constellation:
    def __init(self):
        self.db = None

mySky = StarData()
star = mySky.find_star(attribute = "id", value = "1713")

star_coord = SkyCoord(ra = float(star["ra"]) * u.degree, dec = float(star["dec"]) * u.degree) 

# replace with gps coords
curr_location = EarthLocation(lat=41.3*u.deg, lon=-74*u.deg, height=390*u.m)

# time is stored in UTC - replace with current time
curr_time = Time('2012-7-12 23:00:00')

# find altitude / azimuth location of star
star_altaz = star_coord.transform_to(AltAz(obstime=curr_time,location=curr_location))
print(f"Location of Star {star['id']}: Altitude: {star_altaz.alt:,.3}, Azimuth: {star_altaz.az:,.3}")