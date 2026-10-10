filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    if 'python' in line:
        line = line.replace('python', 'python2')
        print(line)
