rivers = {'severn': 'wales', 'thames': 'england', 'nile': 'egypt'}

for key,value in rivers.items():
    print(key.title())
    print(value.title())
    print("The " + key.title() + " is a river in " + value.title() + ".")
