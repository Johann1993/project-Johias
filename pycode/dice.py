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
        return num








