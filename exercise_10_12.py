import json

FILENAME = 'favnum.json'


def greet():
    try:
        with open(FILENAME) as file:
            num = json.load(file)
    except FileNotFoundError:
        num = int(input("Enter your favourite number: "))
        with open(FILENAME, 'w') as file:
            json.dump(num, file)
        print("Number saved")
    else:
        print("Your favourite number is " + str(num))


greet()