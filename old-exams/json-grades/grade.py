import json
res = {}

def average(ns):
    return sum(ns) / len(ns)

with open("input.json") as f:
    data = json.load(f)

for thing in data:
    sid = thing["id"]
    avg = thing["grades"]
    res[sid] = round(average(avg))

with open("output.txt", "w+") as out:
    for student in dict(sorted(res.items(),key=lambda item: item[0],reverse=False)):
        out.write(f"{student} {res[student]}\n")