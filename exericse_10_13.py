import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username


def greet_user():
    username = get_stored_username()
    answer = input("Are you the last user?" + username + "?")
    if answer == "yes":
        print("Welcome " + username)
    else:
        username = get_new_username()
        print("We will rememebr your username")

greet_user()
