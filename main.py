import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
import json

number = "+880177777777"   

 
bd_number = phonenumbers.parse(number, "BD")

location = geocoder.description_for_number(bd_number, "en")
print("Location:", location)

 
carrier_name = carrier.name_for_number(bd_number, "en")
print("Carrier:", carrier_name)

key = "79da0892597b4706a64462a528239657"

geocoder = OpenCageGeocode(key)

 
query = location
results = geocoder.geocode(query)
if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat)
    print("Longitude:", lng)
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")
    print("Map saved as mylocation.html")
else:
    print("Location not found or no coordinates available")
