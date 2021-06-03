import re
res = {}
i =0
with open("..\exam-schedule.csv") as file:
    for line in file:
        if i==0:
            i=1
            continue
        lArr = line.split(",")
        if lArr[len(lArr)-2] in res:
            res[lArr[len(lArr)-2]] +=1
        else:
            res[lArr[len(lArr)-2]] =1
        
for student in dict(sorted(res.items(),key=lambda item: item[1],reverse=True)):
    print(f"{student} has {res[student]} exams")
    break