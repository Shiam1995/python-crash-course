from Admin_Module import *

class Privilege:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privilege(['can post', 'can delete'])

