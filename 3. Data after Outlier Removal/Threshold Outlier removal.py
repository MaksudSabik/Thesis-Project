import pandas as pd
import numpy as np
import json
import csv
import math
import glob

'''
obj=[]
for i in range(48):
    name='output'+str(i)+'.csv'
    file = open(name, 'a', newline='',encoding='utf8')
    fileObj = 'obj' + str(i)
    fileObj = csv.writer(file, delimiter=',')
    obj.append(fileObj)
    data = ['Location','Time', 'Intensity']
    fileObj.writerow(data)

'''


dic =  [0 for i in range(48)]

files=glob.glob('../*')

for file in files:
    file = file[3:]

    timearray = ['00.00 - 00.30',
            '00.30 - 01.00',
            '01.00 - 01.30',
            '01.30 - 02.00',
            '02.00 - 02.30',
            '02.30 - 03.00',
            '03.00 - 03.30',
            '03.30 - 04.00',
            '04.00 - 04.30',
            '04.30 - 05.00',
            '05.00 - 05.30',
            '05.30 - 06.00',
            '06.00 - 06.30',
            '06.30 - 07.00',
            '07.00 - 07.30',
            '07.30 - 08.00',
            '08.00 - 08.30',
            '08.30 - 09.00',
            '09.00 - 09.30',
            '09.30 - 10.00',
            '10.00 - 10.30',
            '10.30 - 11.00',
            '11.00 - 11.30',
            '11.30 - 12.00',
            '12.00 - 12.30',
            '12.30 - 13.00',
            '13.00 - 13.30',
            '13.30 - 14.00',
            '14.00 - 14.30',
            '14.30 - 15.00',
            '15.00 - 15.30',
            '15.30 - 16.00',
            '16.00 - 16.30',
            '16.30 - 17.00',
            '17.00 - 17.30',
            '17.30 - 18.00',
            '18.00 - 18.30',
            '18.30 - 19.00',
            '19.00 - 19.30',
            '19.30 - 20.00',
            '20.00 - 20.30',
            '20.30 - 21.00',
            '21.00 - 21.30',
            '21.30 - 22.00',
            '22.00 - 22.30',
            '22.30 - 23.00',
            '23.00 - 23.30',
            '23.30 - 23.59',
            ]
    value = []
    num = []
    xi = [[] for i in range(48)]
    l = []
    for i in range(48):
        value.append(0)
        num.append(0)
        xi.append(l)
    filename = file
    '''
    file = open(filename, 'a', newline='', encoding='utf8')
    fileObj = csv.writer(file, delimiter=',')
    data = ['Time', 'Intensity']
    fileObj.writerow(data)
    '''
    new = '../'+filename
    if filename == 'Code':
        continue
    #print(filename)
    mainCsv = pd.read_csv(new)

    row = len(mainCsv)

    for i in range(row):
        data = mainCsv.iloc[i]

        timeinfo = data['Time']
        time = timeinfo[11:19]
        intensity = data['Intensity']
        path = data['Path']
        cost = data['Cost']
        roadlen = data['RoadSize']
        speed = data['ExpectedSpeed']

        if time >= "00:00:00" and time < "00:30:00" :
            value[0]=value[0] + float(intensity)
            num[0] = num[0] + 1
            xi[0].append(float(intensity))

        if time >= "00:30:00" and time < "01:00:00" :
            value[1] = value[1] + float(intensity)
            num[1] = num[1] + 1
            xi[1].append(float(intensity))


        if time >= "01:00:00" and time < "01:30:00" :
            value[2] = value[2] + float(intensity)
            num[2] = num[2] + 1
            xi[2].append(float(intensity))

        if time >= "01:30:00" and time < "02:00:00" :
            value[3] = value[3] + float(intensity)
            num[3] = num[3] + 1
            xi[3].append(float(intensity))

        if time >= "02:00:00" and time < "02:30:00" :
            value[4] = value[4] + float(intensity)
            num[4] = num[4] + 1
            xi[4].append(float(intensity))

        if time >= "02:30:00" and time < "03:00:00" :
            value[5] = value[5] + float(intensity)
            num[5] = num[5] + 1
            xi[5].append(float(intensity))

        if time >= "03:00:00" and time < "03:30:00" :
            value[6] = value[6] + float(intensity)
            num[6] = num[6] + 1
            xi[6].append(float(intensity))

        if time >= "03:30:00" and time < "04:00:00" :
            value[7] = value[7] + float(intensity)
            num[7] = num[7] + 1
            xi[7].append(float(intensity))

        if time >= "04:00:00" and time < "04:30:00" :
            value[8] = value[8] + float(intensity)
            num[8]= num[8] + 1
            xi[8].append(float(intensity))

        if time >= "04:30:00" and time < "05:00:00" :
            value[9] = value[9] + float(intensity)
            num[9] = num[9] + 1
            xi[9].append(float(intensity))

        if time >= "05:00:00" and time < "05:30:00" :
            value[10] = value[10] + float(intensity)
            num[10] = num[10] + 1
            xi[10].append(float(intensity))

        if time >= "05:30:00" and time < "06:00:00" :
            value[11] = value[11] + float(intensity)
            num[11] = num[11] + 1
            xi[11].append(float(intensity))

        if time >= "06:00:00" and time < "06:30:00" :
            value[12] = value[12] + float(intensity)
            num[12] = num[12] + 1
            xi[12].append(float(intensity))

        if time >= "06:30:00" and time < "07:00:00" :
            value[13] += float(intensity)
            num[13] = num[13] + 1
            xi[13].append(float(intensity))

        if time >= "07:00:00" and time < "07:30:00" :
            value[14] = value[14] + float(intensity)
            num[14] = num[14] + 1
            xi[14].append(float(intensity))

        if time >= "07:30:00" and time < "08:00:00" :
            value[15] = value[15] + float(intensity)
            num[15] = num[15] + 1
            xi[15].append(float(intensity))

        if time >= "08:00:00" and time < "08:30:00" :
            value[16] = value[16] + float(intensity)
            num[16] = num[16] + 1
            xi[16].append(float(intensity))

        if time >= "08:30:00" and time < "09:00:00" :
            value[17] = value[17] + float(intensity)
            num[17] = num[17] + 1
            xi[17].append(float(intensity))

        if time >= "09:00:00" and time < "09:30:00" :
            value[18] = value[18] + float(intensity)
            num[18] = num[18] + 1
            xi[18].append(float(intensity))

        if time >= "09:30:00" and time < "10:00:00" :
            value[19] = value[19] + float(intensity)
            num[19] = num[19] + 1
            xi[19].append(float(intensity))

        if time >= "10:00:00" and time < "10:30:00" :
            value[20] = value[20] + float(intensity)
            num[20] = num[20] + 1
            xi[20].append(float(intensity))

        if time >= "10:30:00" and time < "11:00:00" :
            value[21] = value[21] + float(intensity)
            num[21] = num[21] + 1
            xi[21].append(float(intensity))


        if time >= "11:00:00" and time < "11:30:00" :
            value[22] = value[22] + float(intensity)
            num[22] = num[22] + 1
            xi[22].append(float(intensity))

        if time >= "11:30:00" and time < "12:00:00" :
            value[23] = value[23] + float(intensity)
            num[23] = num[23] + 1
            xi[23].append(float(intensity))

        if time >= "12:00:00" and time < "12:30:00" :
            value[24] = value[24] + float(intensity)
            num[24] = num[24] + 1
            xi[24].append(float(intensity))

        if time >= "12:30:00" and time < "13:00:00" :
            value[25] = value[25] + float(intensity)
            num[25] = num[25] + 1
            xi[25].append(float(intensity))

        if time >= "13:00:00" and time < "13:30:00" :
            value[26] = value[26] + float(intensity)
            num[26] = num[26] + 1
            xi[26].append(float(intensity))

        if time >= "13:30:00" and time < "14:00:00" :
            value[27] = value[27] + float(intensity)
            num[27] = num[27] + 1
            xi[27].append(float(intensity))

        if time >= "14:00:00" and time < "14:30:00" :
            value[28] = value[28] + float(intensity)
            num[28] = num[28] + 1
            xi[28].append(float(intensity))

        if time >= "14:30:00" and time < "15:00:00" :
            value[29] = value[29] + float(intensity)
            num[29] = num[29] + 1
            xi[29].append(float(intensity))

        if time >= "15:00:00" and time < "15:30:00" :
            value[30] = value[30] + float(intensity)
            num[30] = num[30] + 1
            xi[30].append(float(intensity))

        if time >= "15:30:00" and time < "16:00:00" :
            value[31] = value[31] + float(intensity)
            num[31] = num[31] + 1
            xi[31].append(float(intensity))


        if time >= "16:00:00" and time < "16:30:00" :
            value[32] = value[32] + float(intensity)
            num[32] = num[32] + 1
            xi[32].append(float(intensity))

        if time >= "16:30:00" and time < "17:00:00" :
            value[33] = value[33] + float(intensity)
            num[33] = num[33] + 1
            xi[33].append(float(intensity))

        if time >= "17:00:00" and time < "17:30:00" :
            value[34] = value[34] + float(intensity)
            num[34] = num[34] + 1
            xi[34].append(float(intensity))

        if time >= "17:30:00" and time < "18:00:00" :
            value[35] = value[35] + float(intensity)
            num[35] = num[35] + 1
            xi[35].append(float(intensity))

        if time >= "18:00:00" and time < "18:30:00" :
            value[36] = value[36] + float(intensity)
            num[36] = num[36] + 1
            xi[36].append(float(intensity))

        if time >= "18:30:00" and time < "19:00:00" :
            value[37] = value[37] + float(intensity)
            num[37] = num[37] + 1
            xi[37].append(float(intensity))

        if time >= "19:00:00" and time < "19:30:00" :
            value[38] = value[38] + float(intensity)
            num[38] = num[38] + 1
            xi[38].append(float(intensity))

        if time >= "19:30:00" and time < "20:00:00" :
            value[39] = value[39] + float(intensity)
            num[39] = num[39] + 1
            xi[39].append(float(intensity))


        if time >= "20:00:00" and time < "20:30:00" :
            value[40] = value[40] + float(intensity)
            num[40] = num[40] + 1
            xi[40].append(float(intensity))

        if time >= "20:30:00" and time < "21:00:00" :
            value[41] = value[41] + float(intensity)
            num[41] = num[41] + 1
            xi[41].append(float(intensity))

        if time >= "21:00:00" and time < "21:30:00" :
            value[42] = value[42] + float(intensity)
            num[42] = num[42] + 1
            xi[42].append(float(intensity))

        if time >= "21:30:00" and time < "22:00:00" :
            value[43] = value[43] + float(intensity)
            num[43] = num[43] + 1
            xi[43].append(float(intensity))

        if time >= "22:00:00" and time < "22:30:00" :
            value[44] = value[44] + float(intensity)
            num[44] = num[44] + 1
            xi[44].append(float(intensity))

        if time >= "22:30:00" and time < "23:00:00" :
            value[45] = value[45] + float(intensity)
            num[45] = num[45] + 1
            xi[45].append(float(intensity))

        if time >= "23:00:00" and time < "23:30:00" :
            value[46] = value[46] + float(intensity)
            num[46] = num[46] + 1
            xi[46].append(float(intensity))

        if time >= "23:30:00" and time < "23:59:59" :
            value[47] = value[47] + float(intensity)
            num[47] = num[47] + 1
            xi[47].append(float(intensity))

    outlier1 = [0 for m in range(48)]
    outlier2 = [0 for m in range(48)]
    timecount = [0 for m in range(48)]

    tuple = 0
    for j in range(48):
        if num[j] >= 5:
            avg = value[j]/num[j]
            total = 0
            for k in range(len(xi[j])):
                total = total + (xi[j][k]-avg)*(xi[j][k]-avg)

            dev = total/num[j]
            dev = math.sqrt(dev)
            outlier1[j] = avg - (2*dev)
            outlier2[j] = avg + (2 * dev)
            tuple = 1
            #data = [timearray[j],avg,dev,num[j]]
            #fileObj.writerow(data)
            timecount[j] = num[j]




    if tuple == 1:
        file = open(filename, 'a', newline='', encoding='utf8')
        fileObj = csv.writer(file, delimiter=',')
        data = ['Time', 'Intensity','Data','Path','RoadLength','ExpectedSpeed','Cost']
        fileObj.writerow(data)


        for i in range(row):
            data = mainCsv.iloc[i]

            timeinfo = data['Time']
            time = timeinfo[11:19]
            intensity = data['Intensity']
            path = data['Path']
            cost = data['Cost']
            roadlen = data['RoadSize']
            speed = data['ExpectedSpeed']

            if time >= "00:00:00" and time < "00:30:00" and float(intensity)>=outlier1[0] and  float(intensity)<=outlier2[0] and timecount[0] != 0:
                data = [timeinfo,intensity,timecount[0],path,roadlen,speed,cost]
                fileObj.writerow(data)

            if time >= "00:30:00" and time < "01:00:00" and float(intensity)>=outlier1[1] and  float(intensity)<=outlier2[1] and timecount[1] != 0 :
                data = [timeinfo, intensity, timecount[1], path, roadlen, speed, cost]
                fileObj.writerow(data)


            if time >= "01:00:00" and time < "01:30:00"  and float(intensity)>=outlier1[2] and  float(intensity)<=outlier2[2] and timecount[2] != 0:
                data = [timeinfo, intensity, timecount[2], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "01:30:00" and time < "02:00:00"  and float(intensity)>=outlier1[3] and  float(intensity)<=outlier2[3] and timecount[3] != 0:
                data = [timeinfo, intensity, timecount[3], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "02:00:00" and time < "02:30:00"  and float(intensity)>=outlier1[4] and  float(intensity)<=outlier2[4] and timecount[4] != 0:
                data = [timeinfo, intensity, timecount[4], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "02:30:00" and time < "03:00:00"  and float(intensity)>=outlier1[5] and  float(intensity)<=outlier2[5] and timecount[5] != 0:
                data = [timeinfo, intensity, timecount[5], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "03:00:00" and time < "03:30:00"  and float(intensity)>=outlier1[6] and  float(intensity)<=outlier2[6] and timecount[6] != 0:
                data = [timeinfo, intensity, timecount[6], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "03:30:00" and time < "04:00:00"  and float(intensity)>=outlier1[7] and  float(intensity)<=outlier2[7] and timecount[7] != 0:
                data = [timeinfo, intensity, timecount[7], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "04:00:00" and time < "04:30:00"  and float(intensity)>=outlier1[8] and  float(intensity)<=outlier2[8] and timecount[8] != 0:
                data = [timeinfo, intensity, timecount[8], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "04:30:00" and time < "05:00:00"  and float(intensity)>=outlier1[9] and  float(intensity)<=outlier2[9] and timecount[9] != 0:
                data = [timeinfo, intensity, timecount[9], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "05:00:00" and time < "05:30:00"  and float(intensity)>=outlier1[10] and  float(intensity)<=outlier2[10] and timecount[10] != 0:
                data = [timeinfo, intensity, timecount[10], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "05:30:00" and time < "06:00:00"  and float(intensity)>=outlier1[11] and  float(intensity)<=outlier2[11] and timecount[11] != 0:
                data = [timeinfo, intensity, timecount[11], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "06:00:00" and time < "06:30:00"  and float(intensity)>=outlier1[12] and  float(intensity)<=outlier2[12] and timecount[12] != 0:
                data = [timeinfo, intensity, timecount[12], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "06:30:00" and time < "07:00:00"  and float(intensity)>=outlier1[13] and  float(intensity)<=outlier2[13] and timecount[13] != 0:
                data = [timeinfo, intensity, timecount[13], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "07:00:00" and time < "07:30:00"  and float(intensity)>=outlier1[14] and  float(intensity)<=outlier2[14] and timecount[14] != 0:
                data = [timeinfo, intensity, timecount[14], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "07:30:00" and time < "08:00:00"  and float(intensity)>=outlier1[15] and  float(intensity)<=outlier2[15] and timecount[15] != 0:
                data = [timeinfo, intensity, timecount[15], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "08:00:00" and time < "08:30:00"  and float(intensity)>=outlier1[16] and  float(intensity)<=outlier2[16] and timecount[16] != 0:
                data = [timeinfo, intensity, timecount[16], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "08:30:00" and time < "09:00:00"  and float(intensity)>=outlier1[17] and  float(intensity)<=outlier2[17] and timecount[17] != 0:
                data = [timeinfo, intensity, timecount[17], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "09:00:00" and time < "09:30:00"  and float(intensity)>=outlier1[18] and  float(intensity)<=outlier2[18] and timecount[18] != 0:
                data = [timeinfo, intensity, timecount[18], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "09:30:00" and time < "10:00:00"  and float(intensity)>=outlier1[19] and  float(intensity)<=outlier2[19] and timecount[19] != 0:
                data = [timeinfo, intensity, timecount[19], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "10:00:00" and time < "10:30:00"  and float(intensity)>=outlier1[20] and  float(intensity)<=outlier2[20] and timecount[20] != 0:
                data = [timeinfo, intensity, timecount[20], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "10:30:00" and time < "11:00:00"  and float(intensity)>=outlier1[21] and  float(intensity)<=outlier2[21] and timecount[21] != 0:
                data = [timeinfo, intensity, timecount[21], path, roadlen, speed, cost]
                fileObj.writerow(data)


            if time >= "11:00:00" and time < "11:30:00"  and float(intensity)>=outlier1[22] and  float(intensity)<=outlier2[22] and timecount[22] != 0:
                data = [timeinfo, intensity, timecount[22], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "11:30:00" and time < "12:00:00"  and float(intensity)>=outlier1[23] and  float(intensity)<=outlier2[23] and timecount[23] != 0:
                data = [timeinfo, intensity, timecount[23], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "12:00:00" and time < "12:30:00"  and float(intensity)>=outlier1[24] and  float(intensity)<=outlier2[24] and timecount[24] != 0:
                data = [timeinfo, intensity, timecount[24], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "12:30:00" and time < "13:00:00"  and float(intensity)>=outlier1[25] and  float(intensity)<=outlier2[25] and timecount[25] != 0:
                data = [timeinfo, intensity, timecount[25], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "13:00:00" and time < "13:30:00"  and float(intensity)>=outlier1[26] and  float(intensity)<=outlier2[26] and timecount[26] != 0:
                data = [timeinfo, intensity, timecount[26], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "13:30:00" and time < "14:00:00"  and float(intensity)>=outlier1[27] and  float(intensity)<=outlier2[27] and timecount[27] != 0:
                data = [timeinfo, intensity, timecount[27], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "14:00:00" and time < "14:30:00"  and float(intensity)>=outlier1[28] and  float(intensity)<=outlier2[28] and timecount[28] != 0:
                data = [timeinfo, intensity, timecount[28], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "14:30:00" and time < "15:00:00"  and float(intensity)>=outlier1[29] and  float(intensity)<=outlier2[29] and timecount[29] != 0:
                data = [timeinfo, intensity, timecount[29], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "15:00:00" and time < "15:30:00"  and float(intensity)>=outlier1[30] and  float(intensity)<=outlier2[30] and timecount[30] != 0:
                data = [timeinfo, intensity, timecount[30], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "15:30:00" and time < "16:00:00"  and float(intensity)>=outlier1[31] and  float(intensity)<=outlier2[31] and timecount[31] != 0:
                data = [timeinfo, intensity, timecount[31], path, roadlen, speed, cost]
                fileObj.writerow(data)


            if time >= "16:00:00" and time < "16:30:00"  and float(intensity)>=outlier1[32] and  float(intensity)<=outlier2[32] and timecount[32] != 0:
                data = [timeinfo, intensity, timecount[32], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "16:30:00" and time < "17:00:00"  and float(intensity)>=outlier1[33] and  float(intensity)<=outlier2[33] and timecount[33] != 0:
                data = [timeinfo, intensity, timecount[33], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "17:00:00" and time < "17:30:00"  and float(intensity)>=outlier1[34] and  float(intensity)<=outlier2[34] and timecount[34] != 0:
                data = [timeinfo, intensity, timecount[34], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "17:30:00" and time < "18:00:00"  and float(intensity)>=outlier1[35] and  float(intensity)<=outlier2[35] and timecount[35] != 0:
                data = [timeinfo, intensity, timecount[35], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "18:00:00" and time < "18:30:00"  and float(intensity)>=outlier1[36] and  float(intensity)<=outlier2[36] and timecount[36] != 0:
                data = [timeinfo, intensity, timecount[36], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "18:30:00" and time < "19:00:00"  and float(intensity)>=outlier1[37] and  float(intensity)<=outlier2[37] and timecount[37] != 0:
                data = [timeinfo, intensity, timecount[37], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "19:00:00" and time < "19:30:00"  and float(intensity)>=outlier1[38] and  float(intensity)<=outlier2[38] and timecount[38] != 0:
                data = [timeinfo, intensity, timecount[38], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "19:30:00" and time < "20:00:00"  and float(intensity)>=outlier1[39] and  float(intensity)<=outlier2[39] and timecount[39] != 0:
                data = [timeinfo, intensity, timecount[39], path, roadlen, speed, cost]
                fileObj.writerow(data)


            if time >= "20:00:00" and time < "20:30:00"  and float(intensity)>=outlier1[40] and  float(intensity)<=outlier2[40] and timecount[40] != 0:
                data = [timeinfo, intensity, timecount[40], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "20:30:00" and time < "21:00:00"  and float(intensity)>=outlier1[41] and  float(intensity)<=outlier2[41] and timecount[41] != 0:
                data = [timeinfo, intensity, timecount[41], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "21:00:00" and time < "21:30:00"  and float(intensity)>=outlier1[42] and  float(intensity)<=outlier2[42] and timecount[42] != 0:
                data = [timeinfo, intensity, timecount[42], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "21:30:00" and time < "22:00:00"  and float(intensity)>=outlier1[43] and  float(intensity)<=outlier2[43] and timecount[43] != 0:
                data = [timeinfo, intensity, timecount[43], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "22:00:00" and time < "22:30:00"  and float(intensity)>=outlier1[44] and  float(intensity)<=outlier2[44] and timecount[44] != 0:
                data = [timeinfo, intensity, timecount[44], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "22:30:00" and time < "23:00:00"  and float(intensity)>=outlier1[45] and  float(intensity)<=outlier2[45] and timecount[45] != 0:
                data = [timeinfo, intensity, timecount[45], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "23:00:00" and time < "23:30:00"  and float(intensity)>=outlier1[46] and  float(intensity)<=outlier2[46] and timecount[46] != 0:
                data = [timeinfo, intensity, timecount[46], path, roadlen, speed, cost]
                fileObj.writerow(data)

            if time >= "23:30:00" and time < "23:59:59"  and float(intensity)>=outlier1[47] and  float(intensity)<=outlier2[47] and timecount[47] != 0:
                data = [timeinfo, intensity, timecount[47], path, roadlen, speed, cost]
                fileObj.writerow(data)

        file.close()


