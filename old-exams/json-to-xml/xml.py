import json
res = {}


with open("input.json") as f:
    data = json.load(f)

for thing in data:
    sid = thing["id"]
    avg = thing["grades"]
    res[sid] = avg

with open("output.txt", "w+") as out:
    out.write(f"<students>\n")
    for student in dict(res.items()):
        out.write(f'<student id="{student}"><grades>')
        for grade in res[student]:
            out.write(f'<grade>{grade}</grade>')
        out.write(f'</grades></student>\n')
    out.write(f'</students>')
    