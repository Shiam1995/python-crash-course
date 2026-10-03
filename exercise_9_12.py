from Admin_Module import *
from priv_admin import *


user = Admin("S", "Chuttoo", "31", 'LDN')

print(user.first_name)
user.privileges.show_privileges()