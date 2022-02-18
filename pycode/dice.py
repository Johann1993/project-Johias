# our dice class for creating a dice to use in game

import random


class Dice():

    max_amount = 6

    def __init__(self):
        random.seed()
        self.my_rolls_amount = 0
        self.total_amount = 0

    def roll_the_dice(self):
        num = random.randint(1, self.max_amount)
        self.total_amount += num
        self.my_rolls_amount += 1
        #print("you got"+ num + "and now got total of " + self.total_amount + "throws. continue playing?")
        return num

    def show_total(self):
        return self.total_amount
        







