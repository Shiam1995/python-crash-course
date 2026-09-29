person_1 = {
    'first_name': 'Sarah',
    'last_name': 'Doe',
    'age': 21,
    'city': 'London'
}

person_2 = {
    'first_name': 'Johh',
    'last_name': 'Doe',
    'age': 22,
    'city': 'London'
}

person_3 = {
    'first_name': 'Sam',
    'last_name': 'Doe',
    'age': 23,
    'city': 'London'


}

list_of_people = [person_1, person_2, person_3]

for person in list_of_people:
    print(person)

for person in list_of_people:
    print(person['first_name'])
