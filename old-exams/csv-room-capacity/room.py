import re

check = []
checked = []
reparsed = {}
res = {}
skip=True

with open("exam-schedule.csv") as f:
    for line in f:
        if skip:
            skip=False
            continue
        row = line.split(",")
        room = row[len(row)-1].replace("\n","")
        date = row[3]
        time = row[5]
        bruh = " ".join([room, date, time])
        check.append(bruh)
    f.close()

check.sort(key=None)
for thing in check:
    if thing not in checked:
        checked.append(thing)
        reparsed[thing] = {"count":1}
    else:
        reparsed[thing]["count"]+=1
print(reparsed)
pList = list(reparsed.items())

for thing in pList:
    bruh =re.sub(r'(\d{2}-\d{2}-\d{2} \w{2})',"", thing[0])
    if bruh not in res:
        res[bruh] = thing[1]["count"]
    else:
        if thing[1]["count"]>res[bruh]:
            res[bruh] = thing[1]["count"]
    
print(res)
with open("output.txt", "w+") as f:
    for thing in res:
        f.write(thing + str(res[thing]) + "\n")
