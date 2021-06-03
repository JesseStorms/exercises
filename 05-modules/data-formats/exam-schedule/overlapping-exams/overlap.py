import re
res = {}
i =0
with open("..\exam-schedule.csv") as file:
    for line in file:
        if i==0:
            i=1
            continue
        lArr = line.split(",")
        cThing = lArr[len(lArr)-2] + " | " + lArr[3] + " | " + lArr[5]
        if cThing in res:
            res[cThing] +=1
            # print(cThing)
        else:
            res[cThing] =1



for student in dict(sorted(res.items(),key=lambda item: item[1],reverse=True)):
    if res[student] == 1:
        continue
    line = student.split("|")
    print(f"{line[0]}has {res[student]} exams on{line[1]}({line[2]})")
    