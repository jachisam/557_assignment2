#!/usr/bin/env python
# coding: utf-8

# In[118]:


import csv
import datetime
from datetime import datetime

with open('1.csv') as csvfile:
    data = list(csv.reader(csvfile))

locations = list()
datetimeFormat = '%m/%d/%y %H:%M'
nI = len(data)

for index in range(2,nI):
    date2 = data[index]
    date1 = data[index -1]
    date2timestamp = datetime.strptime(date2[0], datetimeFormat)
    date1timestamp =  datetime.strptime(date1[0], datetimeFormat)
    diff = date2timestamp - date1timestamp
    minutesInt = int(diff.total_seconds() / 60)
 
    if minutesInt > 3:
        #(carID,DateVisted ,TimeSpent, Latitude, Longitude)
        locations.append((date1[1],date1[0],diff, date1[3], date1[2]))


with open('stop1.csv', 'w') as csvfile2:
    writer = csv.writer(csvfile2, delimiter=',')

    for row in locations:
        writer.writerow(row)

        import math
def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

employees = []
locations = []
    
with open('stop1.csv', 'rw') as a, open('stop1_.csv', 'w') as c, open('locations.csv', 'r') as b:
    reader = csv.reader(a, delimiter=',')
    reader2 = csv.reader(b, delimiter=',')
    writer = csv.writer(c, delimiter=',')

    
    for row in reader:
        employees.append(row)
    
    for location in reader2:
        locations.append(location)
    
    for l in locations:
        for e in employees:
            if '%.4f'%(float(e[4])) == l[1] and '%.3f'%(float(e[3])) == '%.3f'%(float(l[0])):
                e.append(l[2])

    for e in employees:
        writer.writerow(e)


# In[ ]:





# In[ ]:





# In[ ]:




