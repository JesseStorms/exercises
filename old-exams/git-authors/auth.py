import re
import sys

data = sys.stdin.readlines()
commits = []
res = {}

for line in data:
    if re.match(r"(Author: )",line):
        check = re.sub(r"(Author: )","",line)
        name = check.split("<")[0]
        if name in res:
            continue
        else:
            res[name]=1

for man in dict(sorted(res.items(),key=lambda item: item[0],reverse=False)):
    print(f"{man.strip()}")