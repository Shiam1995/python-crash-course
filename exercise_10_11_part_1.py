import json

num = input("Enter a number: ")

filename = 'favnum.json'
with open(filename, 'w') as file:
    json.dump(num, file)
