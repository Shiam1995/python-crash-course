names = ['admin', 'bob', 'charlie', 'derek', 'ethan']
e_name = []


if e_name:
    print("List is not empty")
else:
    print("List is empty")


for name in names:
    if name == 'admin':
        print("You are admin here is report")
    else:
        print("Hello " + name + " how are you doing?")
