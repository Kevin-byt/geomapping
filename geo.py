import func
from geopy.geocoders import Nominatim
import folium
import pandas as pd
import defs
from getpass import getpass
import mysql.connector as mysql

center = defs.Map_center
map = folium.Map(location=center, zoom_start=defs.Map_zoom)
geolocator = Nominatim(user_agent="my_request")

# ================== GET DATA FROM EXCEL SHEET ============================= #
# file = defs.File_name
# data = pd.read_excel(file)

# for index, data in data.iterrows():
#     address = data[defs.Address_column]    
#     position = geolocator.geocode(address)
#     try:
#         location = [position.latitude, position.longitude]
#         folium.Marker(location, popup = f'Name:{data[defs.First_name_column]}\n Consideration:{data[defs.Consideration_column]}').add_to(map)
#     except:
#         print(f"Address {index+2} not well defined")
#     finally:
#         continue


# ================== GET DATA FROM MYSQL DB ============================= #
db = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="geolocation"
)

mycursor = db.cursor()
query = "SELECT * FROM location"

## getting records from the table
mycursor.execute(query)

## fetching all records from the 'cursor' object
records = mycursor.fetchall()

for id, location, user in records:
    print(location)
    address = location 
    position = geolocator.geocode(address)
    try:
        loc = [position.latitude, position.longitude]
        folium.Marker(loc, popup = f'Name:{user}\n Location:{location}').add_to(map)        
    except:
        print(f"{location} index {id} not well defined")
    finally:       
        continue
   
map.save('index.html')
