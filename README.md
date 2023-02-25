# Ninja Van Code Dojo 2023
### <i> by team RedactedName </i>

## Problem Context
Given NinjaVan's commitment in making sure that the parcels are
delivered to the customers quickly, our team felt that the essence of
time was of utmost importance. After realising that the last mile drivers spend a significant
amount of time finding the appropriate parcels to deliver based on 
their station and locations, we were committed in reducing the idle time that was wasted.
The 1 hour spent daily by drivers in collecting parcels can be better used to (1.) Deliver more parcels within the timespan
of a day or (2.) Allow drivers to end work earlier which can help improve morale and ultimately
deal with worker retention rate.

## Features
### Address Cleansing
With the help of Google API Geocode, we are able to automate the addressing process
to a good approximate by converting the consumer addresses into a lat-long format, which gave us a good sense of which areas the parcels should be sent to.
### K-means clustering to group by density
Using the lat-long data obtained, we are able to utilise k-means clustering to help us identify the best routes for
each driver, while minimising the unevenness of the workload allocated to each driver. We also considered that each parcel
delivery location might not be equal, and thus factored in a weight system that can influence the importance and effort needed
to deliver that particular parcel.
### User interface to observe clustering results
To reflect the clustering results from the k-mean clustering, we utilised the Google Maps API to reflect each parcel point on the
map. The colour coding will reflect the groupings identified by our system and drivers can then proceed with delivery according to
the classified coloured zones.

## Usage
### Address Cleaning
Run the file `accessingCSVLatLong.py` to clean the data according to the demands and preferences

Expected Outcome:

A new CSV file `latlong.csv` will be created with all the lat-long values. Empty fields in the csv file will indicate that
the row of input address cannot be mapped to a specific lat-long value on Google Maps. Such values will be appended
on the `failedlatlong.csv` file which will require manual detection to process and confirm.

### GUI 
#### Button - `Browse`

Attach the relevant CSV file with lat-long values that is intended to be processed.

#### Field - `Minimum Orders`

Input the number of orders that a driver will have to do daily; This represents the minimum workload a driver has to do

#### Field - `Maximum Orders`

Input the limit of maximum orders that a driver can pick up a day. This is the hard cap on the incentives that the driver can 
take on for extra bonuses per day.

#### Field - `Number of Drivers`

Input the number of drivers that the zone has for that day. This would determine the number of clusters that will be generated.

#### Button - `Get Proximity Clusters`

Click on the button for the backend k-means clustering system to generate the clusters, and
present the data sets on the Google Map API.

##### Map

The map represents the data sets grouped by the clustering system.
It is a static image that shows all the points on the map.
In the future, this can be improved into a zoomable map such that the drivers can easily nagivate and zoom in to the areas
that they are tasked to deliver in, making the location marks more useful and visible.

## Acknowledgments

Throughout this event, we have consulted many NinjaVan staff and online materials, and would like to 
express our appreciation for the assistance and guidance throughout.