list_of_lat_long = []
for address in merged_addresses:
    latLong = findLatLong(address)
    #print (latLong)
    list_of_lat_long.append(latLong)
with open('latlong.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for item in list_of_lat_long:
        writer.writerow(item)