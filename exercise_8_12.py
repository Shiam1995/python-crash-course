def make_sandwich(*toppings):
    print('Making sandwich')
    for topping in toppings:
        print("Adding")
        print("-" + topping)
    print("Done")



make_sandwich('apple', 'banana', 'strawberry')
make_sandwich('apple', 'banana', )
make_sandwich('apple', 'banana','bacon', 'lettuce')
