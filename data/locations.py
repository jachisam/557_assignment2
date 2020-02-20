import csv
import datetime
from datetime import datetime

with open('101.csv', newline='') as csvfile:
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
        locations.append((date1[1],date1[0],diff, date1[2], date1[3]))


with open('stop101.csv', newline='') as csvfile:
writer = csv.writer(csvfile2, delimiter=',')

for row in locations:
    print(row[4])

        
