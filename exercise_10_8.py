def check_files(file):
    try:
        with open(file) as f:
            content = f.read()
    except FileNotFoundError:
        msg = "File " + file + " does not exist"
        print(msg)
    else:
        words = content.split()
        num_words = len(words)




files = ['catsz.txt', 'dogs.txt']

for file in files:
    check_files(file)