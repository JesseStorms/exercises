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
            res[name]+=1
        else:
            res[name]=1

for man in dict(sorted(res.items(),key=lambda item: item[1],reverse=True)):
    print(f"{man.strip()}: {str(res[man]).strip()}")