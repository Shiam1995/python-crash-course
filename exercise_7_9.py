sandwiches_to_do = ['tuna', 'mayo', 'pastrami', 'chicken', 'pastrami', 'pastrami']
done = []

#print(sandwiches_to_do)


print("Deli ran out of pastrami")
while 'pastrami' in sandwiches_to_do:
    sandwiches_to_do.remove('pastrami')


while sandwiches_to_do:

    sandwich = sandwiches_to_do.pop()
    print("Making " + sandwich + "!")
    done.append(sandwich)


print(sandwiches_to_do)
print(done)