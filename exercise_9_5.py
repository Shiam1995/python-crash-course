class User():
    def __init__(self,first_name,last_name, age, location, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def print_name(self):
        print(self.first_name + " " +self.last_name)

    def age_check(self):
        if self.age >= 18:
            print("Old enough full access")
        else:
            print("You are not old enough")

    def increment_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def reset_login_attempts(self, login_attempts):
        self.login_attempts = 0



    def give_det(self):
        print(self.first_name + " " + self.last_name)
        print(self.age)
        print(self.location)
        print(self.login_attempts)



user_1 = User("Shiam", 'Chuttoo', 18, 'london',0)


#print(user_1)

user_1.increment_login_attempts(12)
print(user_1.login_attempts)


user_1.reset_login_attempts(1)
print(user_1.login_attempts)