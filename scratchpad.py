from threading import active_count

responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ")
    response = input("Would you like to climb someday")

    responses[name] = response

    repeat = input("Would you like to let someone else respond (y/n")
    if repeat == "n":
        polling_active = False

print("\n---- Poll Results---")
for name, response in responses.items():
    print(name + "would like to climb " + response + ".")