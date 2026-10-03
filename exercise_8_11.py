def show_magicians(magicians, great_magicians):
    while magicians:
        name = "the great " + magicians.pop()

        print("Appending\n")

        great_magicians.append(name)



magicians = ['houdini','jp','excel']
great_list = []

great_magicians = show_magicians(magicians, great_list)


print(great_list)

print(magicians)


