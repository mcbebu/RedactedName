import googlemaps # pip install googlemaps
import csv

API_KEY = "API HAS BEEN HIDDEN"

client = googlemaps.Client(API_KEY)

def findLatLong(full_location):
    try:
        data = client.geocode(full_location)
        lat = data[0]['geometry']['location']['lat']
        long = data[0]['geometry']['location']['lng']
        return [lat,long]
    except:
        with open('failedlatlong.csv', 'a', newline='') as file:
            writer = csv.writer(file) 
            writer.writerow([full_location])
        return ("NULL")
    