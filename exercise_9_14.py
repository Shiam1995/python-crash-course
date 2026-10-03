from random import randint

x = randint(1, 10)


class Die():

    def __init__(self, face):
        self.face = face

    def roll(self):
        return randint(1, 6)



dice1 = Die(6);

print(dice1.roll())