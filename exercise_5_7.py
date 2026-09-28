favorite_fruit = ['apple', 'banana', 'orange']

#1
if 'apple' in favorite_fruit:
    print("You must like apple")
#2
if 'pear' in favorite_fruit:
    print("You must like pear")
else:
    print("Do you want to add pear")
#3
if 'banana' in favorite_fruit:
    print("You must like banana")
#4
if 'blueberry' not in favorite_fruit:
    print("You must like not blueberry")

#5

if ('orange' in favorite_fruit and 'banana'
        in favorite_fruit):
    print("You must like orange and banana")
    print("Not a good combo")