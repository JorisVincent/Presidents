import json

with open("presidents.json", 'r') as file:
    presidents = json.load(file)

for entry in presidents:
    print(entry["title"])