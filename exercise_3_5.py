guests = ["Yann LeCunn", "Demis Hassabis", "Geoffrey Hinton"]
unavailable = [guests.pop(1)]
guests.insert(1, "Jurgen")

#id use random but its not in use yet



for i in guests:
    print("hello " + i + " i'd like to invite you to dinner")

for i in unavailable:
    print(i.title() + "cant make it")