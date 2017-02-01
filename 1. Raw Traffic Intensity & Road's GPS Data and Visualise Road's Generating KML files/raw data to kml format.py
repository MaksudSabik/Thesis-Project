import pandas as pd
import numpy as np
import json
import csv
import glob

file = open('output.csv', 'a',newline='')
a = csv.writer(file, delimiter=',')
data = ['Latitude','Longitude','Icon','IconScale','LineStringColor','LineStringWidth']
a.writerow(data)


for filename in glob.glob('*.csv'):
    if filename == 'output.csv':
        continue
    mainCsv = pd.read_csv(filename)

    #print(filename)

    #intensity= mainCsv['Intensity']
    #route = mainCsv['Path']

    row = len(mainCsv)

    IconScale = 0.4
    Icon = 145
    LineStringWidth = 5


    max = 0
    #for i in range(row):
        #data = mainCsv.iloc[i]

    '''
        if len(route) <7:
            continue


        if length > max:
            max = length
            bigrow = i

        #data = [route['coordinates'][0][1], route['coordinates'][0][0], Name, 145, IconScale, LineStringColor, LineStringWidth]
        #a.writerow(data)
    '''

    data = mainCsv.iloc[0]
    LineStringColor = 'yellow'

    route = data['Path']
    route = json.loads(route)
    length = len(route['coordinates'])

    for j in range(length):
        Longitude = route['coordinates'][j][0]
        Latitude = route['coordinates'][j][1]
        Icon = 110
        Name = " "
        if j == 0:
            Icon=145
            #Name = data['OsmName']
        data = [Latitude, Longitude, 110, IconScale, LineStringColor, LineStringWidth]
        a.writerow(data)

    data = [Latitude, Longitude, 110, IconScale, LineStringColor, LineStringWidth]
    a.writerow(data)
    a.writerow([])