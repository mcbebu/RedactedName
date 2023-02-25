import requests
import numpy as np

API_KEY = "AIzaSyA5vF812q_CAOD6UvQwH5zPC9-VkXdFtTU"

def colour_list(colour_num):
    match colour_num:
        case '1.0':
            return "red"
        case '2.0':
            return "blue"
        case '3.0':
            return "green"
        case "4.0":
            return "yellow"
        case "5.0":
            return "orange"
        case "6.0":
            return "purple"
        case "7.0":
            return "grey"
        # Add more cases depending on driver number in area
        case _:
            return "white"

def generate_map(centrepoint, clusters):
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    zoom = 11
    #center = "-6.2250138,106.9004472"
    center = str(centrepoint[0]) + "," + str(centrepoint[1])
    print(center)
    print(clusters[0][0])
    print(clusters)
    print(len(clusters))

    tags = ""
    for counter in range(0,len(clusters)):
        first_lat = clusters[counter][0]
        second_long = clusters[counter][1]
        colour_num = clusters[counter][2]
        print(colour_num)
        colour = colour_list(str(colour_num))
        ##FORMAT = &markers=color:<COLOUR>%7C<LATLONG>%size:mid
        latlong = str(first_lat) + "," + str(second_long)
        tags += "&markers=color:"+ colour +"%7C"+ latlong +'&size:mid'

    print(tags)

    r = requests.get(url + "center=" + center + "&zoom=" +
                    str(zoom) + "&size=400x400" + tags + "&key=" +
                                API_KEY + "&sensor=false")

    # wb mode is stand for write binary mode
    f = open('googlemaps.png', 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    # close method of file object
    # save and close the file
    f.close()