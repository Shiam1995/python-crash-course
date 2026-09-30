age = input("What is your age?")
age = int(age)


if age <= 3:
    print("free")
elif age > 3 and age <= 12:
    print("10 dollars")
else:
    print("15 dollars")