import sys
import math

data = sys.stdin.readlines()
for thing in data:
    result = ''
    thing.replace('\n',"")
    num = int(thing)
    for i in range(32,-1,-1):
        if 2**i <= num:
            bruh=2**i
            num=num-bruh
            result=result+"1"
        else:
            result = result+"0"
    print(result.lstrip('0'))