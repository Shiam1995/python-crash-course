# creating test

# and, or, xor, nor, nand, not, buffer

string_a = "dog"
string_b = "cat"

print(string_a == string_b)
print(string_a == "dog")
print(string_a == "cat")

print(len(string_a) == len(string_b))

number_1 = "10"
number_2 = "20"

print(number_1 == number_2)
print(number_1 != number_2)
print(number_1 > number_2)
print(number_1 >= number_2)


number_3 = "15"
number_4 = "21"

if (number_3 > number_1 and number_3 < number_2):
    print("Number 3 is in range")

if (number_3 > number_2 or number_3 < number_4):
    print("Number 3 is in not the smallest")

sushi = ['salmon', 'karrage',' seabass']

if ('salmon' in sushi):
    print("We have it")
