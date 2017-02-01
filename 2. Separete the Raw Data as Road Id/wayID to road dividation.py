import pandas as pd
import numpy as np
import json
import csv


mainCsv = pd.read_csv('Sep1Sep152015.csv')

row = len(mainCsv)
dic = {}
l=[]
for i in range(row):
    data = mainCsv.iloc[i]

    time = data['TimeStamp']
    #time = timeStamp[11:19]
    intensity = data['InferredIntensity']
    location = data['WayID']
    path = data['Path']
    size = data['distanceKM']
    cost = data['cost']
    speed = data['roadSpeedKMH']

    '''
    char1 = '/' in str(location)
    char2 = '?' in str(location)
    char3 = 'মহাসড়ক' in str(location)
    char4 = 'বিমানবন্দর' in str(location)
    char5 = 'জিয়াউর' in str(location)
    char6 = 'সেতু' in str(location)

    #test = str(location) in l
    if char1 ==False and char2 == False and char3 == False and char4 == False and char5 == False and char6 == False and len(str(location)) > 0:
    '''
    filename = str(location)+'.csv'
    file = open(filename, 'a', newline='', encoding='utf8')
    fileObj = csv.writer(file, delimiter=',')
    t = str(filename) in dic
    if t == False:
        data = ['WayId','Time', 'Intensity', 'Path','RoadSize','Cost','ExpectedSpeed']
        fileObj.writerow(data)
    data = [location,time, intensity,path,size,cost,speed]
    fileObj.writerow(data)
    dic[str(filename)] = 1
    file.close()
