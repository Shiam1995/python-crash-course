filename = 'guest_book.txt'
with open(filename, 'w') as f:
    while True:
        name = input("What is your name? ")
        if name == 'q':
            break
        else:
            f.write(name)
            f.write("\n")
f.close()
