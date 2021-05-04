import sys
import re



data = sys.stdin.readlines()
races = []
ranking = {}

for i in range(0,len(data)//100):
    # races
    races.append("".join(data[i*100:(i+1)*100])) 

for race in races:
    standing = race.split('\n')
    standing.reverse()
    for person in standing:
        if person in ranking:
            ranking[person]=ranking[person]+standing.index(person)
        else:
            ranking[person] = standing.index(person)

result = dict(sorted(ranking.items(),key=lambda item: item[1],reverse=True))
for i in range(0,10):
    print(list(result)[i])
