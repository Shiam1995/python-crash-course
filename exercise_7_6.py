message = "please tell me what pizza you would like press q to quit"



toppings = []

flag = True





while flag:
    topping = input(message)
    toppings.append(topping)
    if topping == "q":
        break




print("Pizza with:")
for topping in toppings:
    print(topping)



"""
while flag:
    topping = input(message)
    toppings.append(topping)
    if topping == "q":
        flag = False
"""




"""
while topping != "q":
    print(topping)
    toppings.append(topping)
    topping = input(message)
"""

#print("Pizza with:")
#for topping in toppings:
#    print(topping)



