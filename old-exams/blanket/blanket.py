import sys
import datetime
import json
from statistics import mean


def getDate(date):
    # sorts on month for some reason?
    return datetime.datetime.strptime(date[0], '%d/%M/%Y')

data = sys.stdin.readline()
jData = json.loads(data)
jList = list(dict.items(jData))
jList.sort(key=getDate)

for date in jList:
    temp = round(mean(date[1]))
    print(temp)
