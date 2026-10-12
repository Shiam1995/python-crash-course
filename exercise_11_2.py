#city and country

def give_me_info(city, country, population = ''):
    if population:
        full_detail = country + " : " + city + " - " + population
    else:
        full_detail = country + " : " + city
    return full_detail


