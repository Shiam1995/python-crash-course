import json

username = input("Enter your username: ")

filename = 'username.json'
with open(filename, 'w') as file:
    json.dump(username, file)
    print("We'll remember when you come back" + username)