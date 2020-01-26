from geopy.geocoders import Nominatim
import geocoder

geolocator = Nominatim()
city = "Khulna"
country = "BD"
loc = geolocator.geocode(city+',' + country)
print("latitude is :", loc.latitude, "longtitude is:", loc.longitude)
g = geocoder.ip('me')
print(g.latlng)