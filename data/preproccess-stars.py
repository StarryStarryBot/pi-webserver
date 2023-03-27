import json
import csv
from pathlib import Path

star_locations = []
database = []

path = Path(__file__).parent / "star-data.csv"

with open(path, newline='') as reader:
    database = [{k: v for k, v in row.items()} for row in csv.DictReader(reader, skipinitialspace=True)]

for star_data in database:
    star = {}
    star["id"] = star_data["id"]
    star["magnitude"] = star_data["mag"]
    star["ra"] = star_data["ra"]
    star["dec"] = star_data["dec"]

    star_locations.append(star)

with open("star-data.json", "w") as outfile:
    json.dump(star_locations, outfile)
