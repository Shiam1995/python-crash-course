


available_toppings = ['mushroom', 'olives', 'green peppers',
                      'pepperoini', 'pineapple', 'extra cheese']

requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we dont have " + requested_topping + ".")

print("Finsihed making your pizza")