guests = ["Yann LeCunn", "Demis Hassabis", "Geoffrey Hinton"]
unavailable = [guests.pop(1)]
guests.insert(1, "Jurgen")

#id use random but its not in use yet



for i in guests:
    print("hello " + i + " i'd like to invite you to dinner")

for i in unavailable:
    print(i.title() + " cant make it")

message = "I have found a bigger space"
print(message)
guests.insert(0, "Jensen")
guests.insert(2, "Lisa")
guests.append("TSMC")

for i in guests:
    print("hello " + i + " i'd like to invite you to dinner")

message = "Unfortunatly space is tight only 2 people can attend"
print(message)
print("------------------")
people_to_inform = []
people_to_inform.append(guests.pop())
people_to_inform.append(guests.pop())
people_to_inform.append(guests.pop())
people_to_inform.append(guests.pop())

print("------------------")
for i in people_to_inform:
    print(i + " apologies space is no longer avaliable")


for i in guests:
    print("hello " + i + " i'd like to invite you to dinner")

del guests[1]
del guests[0]
print("------------------")
for i in guests:
    print("hello " + i + " i'd like to invite you to dinner")