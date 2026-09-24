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
