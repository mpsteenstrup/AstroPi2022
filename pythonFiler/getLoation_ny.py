from orbit import ISS
location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
print(location)

print(f"breddegrader: {location.latitude.degrees}")
print(f"længdegrader: {location.longitude.degrees}")

if location.latitude.degrees>0:
	print("nordlige halvkugle")
else:
	print("sydlige halvkugle")
