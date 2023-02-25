import pandas as pd
import csv
import math
import random

datafile = pd.read_csv("limited_inputs.csv")
latlongdata = pd.read_csv("latlong.csv")
latlongdata.columns = ['lat', 'long']

concated_data = pd.concat([datafile, latlongdata], axis=1)

randomlist = []

for i in range(0, len(concated_data)):
    randomlist.append(random.randint(1, 3))

d = pd.DataFrame(randomlist, columns=['weight'])

concated_data = pd.concat([concated_data, d], axis=1)

concated_data.to_csv(r'C:/Users/leezh/Documents/RedactedName/weighted_data.csv')