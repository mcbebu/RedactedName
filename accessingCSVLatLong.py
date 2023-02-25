import pandas as pd
import csv
import math
from convertLatLong import findLatLong

datafile = pd.read_csv("customer_addresses_id.csv", usecols=['to_address1', 'to_address2'], nrows = 200)
# for testing, will only use 3 random values in the list to run the google api to avoid
# exceeding limit
limited_dataset = pd.read_csv("customer_addresses_id.csv", usecols=['to_address1','to_address2'], nrows=3)
#print (limited_dataset)

merged_addresses = []

for index, row in datafile.iterrows():
    #print(row['to_address2'])
    if (str(row['to_address2']) != "nan"):
        merged_addresses.append(row['to_address1'] + row['to_address2'])
    else:
        merged_addresses.append(row['to_address1'])

list_of_lat_long = []
for address in merged_addresses:
    latLong = findLatLong(address)
    #print (latLong)
    list_of_lat_long.append(latLong)
with open('latlong.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for item in list_of_lat_long:
        if (item == "NULL"):
            writer.writerow([item])
        else:
            writer.writerow(item)