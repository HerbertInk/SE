import phonenumbers
import folium
from My_Number import number
from phonenumbers import geocoder

key = "33932a69ea59437b87466abdfa599760"

sur_number = phonenumbers.parse(number)

ur_location = geocoder.description_for_number(sur_number, "en")
print("Your location: ", ur_location)

# Get service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print("Service Provider: ", carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(ur_location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']
print("Latitude: ", lat, "\nLongitude: ", lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=ur_location).add_to(myMap)

# Map in Html
myMap.save("mylocation.html")
