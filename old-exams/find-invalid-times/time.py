import datetime
import re

result = []
i = 0
def getDate(date):
    # sorts on month for some reason?
    try:
        return datetime.datetime.strftime(datetime.datetime.strptime(date, '%H:%M:%S'),"%H:%M:%S")
    except:
        return False

with open("input.txt") as file:
    for line in file:
        i += 1
        reg = re.findall(r'(\d{2}):(\d{2}):(\d{2})', line)
        # print(reg)
        for match in reg:
            stamp = ":".join(match)
            res = getDate(stamp)
            if not res:
                result.append(str(i) + " " + stamp)
        
file.close()

with open("output.txt", "w+") as f:
    for thing in result:
        f.write(thing+"\n")
f.close()

