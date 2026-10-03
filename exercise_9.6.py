class Resturant():

    def __init__(self,name,cusine):
        self.name = name
        self.cusine = cusine

    def give_details(self):
        print(self.name.title() + " " + self.cusine.title())



class IceCreamStand(Resturant):
    def __init__(self,name,cusine):
        super().__init__(name,cusine)
        self.flavour = ['lemon','apple']

    def print_flavours(self):
        print(self.flavour)



gelato = IceCreamStand("Gelato","ice cream")

print(gelato.name)

gelato.print_flavours()