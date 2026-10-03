class Resturant():

    def __init__(self,name,cuisine,served):
        self.name = name
        self.cuisine = cuisine
        self.served = served

    def give_details(self):
        print(self.name.title() + " " + self.cuisine.title())

    def increment_served(self,served):
        self.served += served

    def print_served(self):
        print(self.served)


resturant_1a = Resturant("shiro","sushi",0)
resturant_1a.print_served()
resturant_1a.served += 1
resturant_1a.increment_served(5)

resturant_1a.print_served()
