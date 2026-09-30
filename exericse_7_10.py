responses = {}

questioning = True


while questioning:

    name = input("What is your name?")
    response = input("What is your favorite place?")

    responses[name] = response

    repeat = input("Would you like to repeat (y/n)?")

    if repeat == "n":
        questioning = False

print("\n--Poll--")
for name, response in responses.items():
    print(name + ": " + response)

