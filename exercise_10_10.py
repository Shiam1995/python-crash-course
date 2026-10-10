
file = 'alice.txt'

with open(file) as f:
    content = f.read()

print(content.count("Alice"))