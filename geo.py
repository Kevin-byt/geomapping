import func
from geopy.geocoders import Nominatim
import folium
import pandas as pd
import defs

file = defs.File_name
data = pd.read_excel(file)

center = defs.Map_center
map = folium.Map(location=center, zoom_start=defs.Map_zoom)
geolocator = Nominatim(user_agent="my_request")

for index, data in data.iterrows():
    address = data[defs.Address_column]    
    position = geolocator.geocode(address)
    try:
        location = [position.latitude, position.longitude]
        folium.Marker(location, popup = f'Name:{data[defs.First_name_column]}\n Consideration:{data[defs.Consideration_column]}').add_to(map)
    except:
        print(f"Address {index+2} not well defined")
    finally:
        continue

map.save('index.html')
