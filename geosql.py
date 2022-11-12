from geopy.geocoders import Nominatim
import folium
import defs
import mysql.connector as mysql

center = defs.Map_center
map = folium.Map(location=center, zoom_start=defs.Map_zoom)
geolocator = Nominatim(user_agent="my_request")

# ================== GET DATA FROM MYSQL DB ============================= #
db = mysql.connect(
    host=defs.host,
    user=defs.user,
    password=defs.pwd,
    database=defs.db
)

mycursor = db.cursor()
query = "SELECT * FROM location"
# getting records from the table
mycursor.execute(query)
# fetching all records from the 'cursor' object
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
   
map.save('mysql.html')
