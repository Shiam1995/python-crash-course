class Resturant():

    def __init__(self,name,cusine):
        self.name = name
        self.cusine = cusine

    def give_details(self):
        print(self.name.title() + " " + self.cusine.title())


resturant_1a = Resturant("shiro","sushi")
resturant_1a.give_details()