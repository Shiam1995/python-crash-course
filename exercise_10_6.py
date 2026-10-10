def num_add():
    try:
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
    except ValueError:
        print("Please enter an integer")
    else:
        print(num_1 + num_2)


num_add()