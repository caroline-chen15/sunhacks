import geopy
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Champ de Mars, Paris, France")
print(location.latitude, location.longitude)
