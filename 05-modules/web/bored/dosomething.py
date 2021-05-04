from urllib.request import urlopen
import json

def get(url):
    with urlopen(url) as res:
        return res.read().decode('UTF-8')
data = get('https://www.boredapi.com/api/activity')
data = json.loads(data)
print(data['activity'])