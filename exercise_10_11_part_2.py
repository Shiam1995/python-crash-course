import json

filename = 'favnum.json'

with open(filename, 'r') as file:
    num = json.load(file)

print(num)