while True:
    num_1 = input("Enter a number (q to quit): ")
    if num_1 == 'q':
        break
    num_2 = input("Enter a number (q to quit): ")
    if num_2 == 'q':
        break

    try:
        total = int(num_1) + int(num_2)
    except ValueError:
        print("Please enter a valid number")
    else:
        print(total)