from urllib.request import urlopen
import json
import sys

def get(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')


data = get(f'https://api.genderize.io/?name={sys.argv[1]}')
data = json.loads(data)

print(f'{data["gender"]}    {data["probability"]*100}%')