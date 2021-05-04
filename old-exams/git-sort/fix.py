import math
import sys
import re
import datetime

def getDate(commit):
    match = re.search(r'Date:   ([0-9 -:]+)',commit)
    return datetime.datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')

data = sys.stdin.readlines()
commits = []

for i in range(0,math.ceil(len(data)/6)):
    c = data[6*i:6*(i+1)]
    commits.append("".join(c))

commits.sort(key=getDate)
commits.reverse()

for commit in commits:
    print(commit, end="")