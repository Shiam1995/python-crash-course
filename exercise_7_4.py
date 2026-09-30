
message = "please tell me what pizza you would like press q to quit"

topping = input(message)

toppings = []


while topping != "q":
    print(topping)
    toppings.append(topping)
    topping = input(message)


print("Pizza with:")
for topping in toppings:
    print(topping)




