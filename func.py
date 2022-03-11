from geopy.geocoders import Nominatim
import pandas as pd

def get_Coords(address):
    location = [0,0]
    geolocator = Nominatim(user_agent="my_request") 
    position = geolocator.geocode(address)

    try:
        location = [position.latitude, position.longitude]
    except:
        print("Invalid Location")
    finally:
        return location
