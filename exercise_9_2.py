class Resturant():

    def __init__(self,name,cusine):
        self.name = name
        self.cusine = cusine

    def give_details(self):
        print(self.name.title() + " " + self.cusine.title())


resturant_1a = Resturant("shiro","sushi")
resturant_1a.give_details()

resturant_1b = Resturant("cafemeow","pancakes")
resturant_1b.give_details()

resturant_1c = Resturant("kungpow","chicken")
resturant_1c.give_details()