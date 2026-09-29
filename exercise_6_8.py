pet_1 = {'species': 'fish',
         'first_name': 'bubbles',
         'last_name': 'the fish',
         'owner': 'Doe'}

pet_2 = {'species': 'cat',
         'first_name': 'meow',
         'last_name': 'huffington',
         'owner': 'Qwan'}

pet_3 = {'species': 'dog',
         'first_name': 'rose',
         'last_name': 'effy',
         'owner': 'april'}

list_of_pet = [pet_1, pet_2,pet_3]

for pet in list_of_pet:
    print(pet['first_name'].title() + " is a " + pet['species'] +
          "who belongs to " + pet['owner'].title())



