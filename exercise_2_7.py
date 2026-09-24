first_name = "    shiam "
middle_name = "    Junior     "
last_name = "chuttoo     "
ending = "!"


print(first_name)
print(middle_name)
print(last_name)

name = first_name + middle_name + last_name + ending

print(name)

first_name = first_name.rstrip()
middle_name = middle_name.rstrip()
last_name = last_name.rstrip()
first_name = first_name.lstrip()
middle_name = middle_name.lstrip()
last_name = last_name.lstrip()

name = first_name + middle_name + last_name + ending
print(name)