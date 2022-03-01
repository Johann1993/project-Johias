"""Python file for generating dice object and functions."""
import random


class Dice():
    """
    Dice class.

    Is used to simulate the
    different functions and objects of
    player statistics and dice.
    """

    max_amount = 6

    def __init__(self):
        """
        Create a dice.

        creates stats of a player/computer.
        """
        random.seed()
        self.my_rolls_amount = 0
        self.total_amount = 0

    def roll_the_dice(self):
        """
        Generate a number.

        Roll dice and add rolls to player total.
        """
        num = random.randint(1, self.max_amount)
        self.my_rolls_amount += 1
        return num

    def roll_dice_cheat(self):
        """
        Get max number on roll.

        This method will generate maximum
        amount avaiable for the dice.
        """
        result = self.max_amount
        return result

    def show_total(self):
        """
        See score.

        Show the total amount
        of points a player has
        at current time in the game.
        """
        return self.total_amount

    def show_amount_rolls(self):
        """See how many rolls player has made."""
        return self.my_rolls_amount

    def add_to_total(self, one_round_total):
        """
        Round total added.

        All points are added to the total
        of the game.
        Method has a parameter for current round points.
        """
        self.total_amount += one_round_total
