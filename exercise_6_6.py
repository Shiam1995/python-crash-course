names = {'lois': 'c', 'peter' : 'java', 'stewiw': 'C++'}

friends = {'Brian', 'Chris', 'Stewie'}

for name in names:
    if name not in friends:
        print(name.title() + ":" + "you should add your info")