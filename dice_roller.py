import random

 # class, dice
 # we will have a method called roll()
 # when we call the fun we will get random tuple


class Dice:

    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second
dice = Dice()
print(dice.roll())