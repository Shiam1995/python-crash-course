class User():
    def __init__(self,first_name,last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def print_name(self):
        print(self.first_name + " " +self.last_name)

    def age_check(self):
        if self.age >= 18:
            print("Old enough full access")
        else:
            print("You are not old enough")

    def give_det(self):
        print(self.first_name + " " + self.last_name)
        print(self.age)
        print(self.location)



user_1 = User("Shiam", 'Chuttoo', 18, 'london' )

print(user_1)

user_1.print_name()
user_1.age_check()
user_1.give_det()

