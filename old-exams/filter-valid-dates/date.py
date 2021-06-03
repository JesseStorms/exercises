import datetime
import re

result = []

def getDate(date):
    try:
        return datetime.datetime.strftime(datetime.datetime.strptime(date, '%d-%m-%Y'),"%#d-%#m-%Y")
        # return datetime.datetime.strftime(datetime.datetime.strptime(date, '%d-%m-%Y'),"%-d-%-m-%Y")
    except:
        return False

with open("input.txt") as file:
    for line in file:
        if re.search(r"-",line):
            res = getDate(line.rstrip())
            if not res:
                continue   
            result.append(res)

file.close()

with open("output.txt", "w+") as f:
    for thing in result:
        f.write(thing+"\n")
f.close()

