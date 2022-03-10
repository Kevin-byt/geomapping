#Importing the Nominatim geocoder class 
from geopy.geocoders import Nominatim
import folium
import pandas as pd

file="data.xlsx"
data = pd.read_excel(file)
# data.head()

center = [-0.0000000, 0.0000000]
map = folium.Map(location=center, zoom_start=2)
geolocator = Nominatim(user_agent="my_request")

for index, data in data.iterrows():
    address = data['Address']    
    position = geolocator.geocode(address)
    location = [position.latitude, position.longitude]
    folium.Marker(location, popup = f'Name:{data["First Name"]}').add_to(map)

map.save('index.html')
