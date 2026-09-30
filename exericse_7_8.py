sandwiches_to_do = ['tuna', 'mayo', 'chicken']
done = []

#print(sandwiches_to_do)


while sandwiches_to_do:

    sandwich = sandwiches_to_do.pop()
    print("Making " + sandwich + "!")
    done.append(sandwich)


print(sandwiches_to_do)
print(done)