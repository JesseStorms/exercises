skip =True
import re
res = {}
with open("exam-schedule.csv") as f:
    for line in f:
        if skip:
            skip=False
            continue
        row = line.split(",")
        type = row[9]
        if type != "S":
            continue

        lid = row[0]
        lSplit = re.findall(r'([\w ]+)', lid)
        print(lSplit)
        for id in lSplit:
            if id not in res:
                res[id] = 1
            else:
                res[id] +=1
    f.close()
res = list(res.items())
res.sort(key=None)
with open("output.txt", "w+") as f:
    for thing in res:
        f.write(thing + str(res[thing]) + "\n")
