import sys
import re


data = sys.stdin.readlines()

for line in data:
    match = re.search(r'([\w ]+):(\d+)\/(\d+).([+-]+)', line)
    totalPoint = int(match.group(3)) + match.group(4).count("+")
    usedPoint = int(match.group(2)) + match.group(4).count("-")
    print(match.group(1)+":"+str(usedPoint)+"/"+str(totalPoint))