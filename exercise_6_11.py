cities = {
    'london' : {
        'name': 'London',
        'population': 10000,
        'fact': 'Thames is the cleanest industrial river'
    },

    'brussels' : {
        'name': 'Brussels',
        'population': 20000,
        'fact': 'Many langauges spoken'
    },

    'delhi': {
        'name': 'Delhi',
        'population': 200000,
        'fact': 'Many langauges spoken'
    }
}

for key, city in cities.items():
    print(city['name'] + " has " + str(city['population']) + " people"
          + " a fun fact is " + city['fact'] + ".")