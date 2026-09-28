usernames = ['admin', 'bob', 'charlie', 'derek', 'ethan']
new_users = ['frank', 'george', 'hendrix', 'BOB', 'ethan']

t_user = [t.lower() for t in usernames]


for new_user in new_users:
    if new_user.lower() in t_user:
        print("Hello " + new_user + " name taken")
    else:
        print("Hello " + new_user + " name available")

