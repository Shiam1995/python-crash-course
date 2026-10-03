def describe_city(city_name = ' ', country = 'earth'):
    print(city_name.title() + " is in " + country.title() )


describe_city(city_name = 'San Francisco', country = 'USA')
describe_city(city_name = 'New York')
describe_city(city_name = 'New York', country = 'USA')