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
        self.my_rolls_amount += 1
        return num

    def roll_dice_cheat(self):
        result = self.max_amount
        return result

    def show_total(self):
        return self.total_amount

    def add_to_total(self,one_round_total):
        self.total_amount += one_round_total


        







