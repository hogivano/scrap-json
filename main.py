import requests
import json

url = "[URL-Link]"
state = 1
index = 1
arr = []

while(url != None and index < 20):
    req = requests.get(url)
    data = req.json()
    arr.extend(data["results"])
    url = data["next"]
    print(index)
    index+=1

with open('data.json', 'w') as outfile:
    json.dump(arr, outfile)

print(len(arr))

print("testing main yeay")
