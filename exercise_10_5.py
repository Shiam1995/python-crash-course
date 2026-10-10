filename = 'programmingpoll'

with open(filename,'w') as f:
    while True:
        reason = input("Enter a reason: ")
        if reason == "q":
            break
        else:
            f.write(reason + "\n")

f.close()