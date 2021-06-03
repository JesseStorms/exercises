import sys

data = sys.stdin.readlines()

for line in data:
    line.strip()
    for thing in line.split(","):
        thing = thing.replace("\n","")
        if len(thing) == 0:
            continue
        print(thing)
 