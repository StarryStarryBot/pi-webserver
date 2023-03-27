from data.DataHandler import StarData

mySky = StarData()
star = mySky.find_star(attribute = "hd", value = "12929")

sky_coordinates = star.get_sky_coordinates()
print(f"Location of Star {star.data['hd']}: Altitude: {sky_coordinates.alt.degree:,.3}, Azimuth: {sky_coordinates.az.degree:,.3}")

coords = f"{abs(sky_coordinates.az.degree):,.3}, {abs(sky_coordinates.alt.degree):,.3}"
print(coords)

closest_stars = mySky.find_closest_stars(2, 30)
for star_id in closest_stars:
    print(mySky.find_star(attribute = "id", value = star_id).data)