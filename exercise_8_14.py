def make_car(brand = ' ', cartype = ' ',color = ' ', **carinfo):
    car = {}
    car['brand'] = brand
    car['cartype'] = type
    car['color'] = color

    for key, value in carinfo.items():
        car[key] = value
    return car


car = make_car("ford", '4*4', 'black', age ='20',
               transmission='auto')
print(car)