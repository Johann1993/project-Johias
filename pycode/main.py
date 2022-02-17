# this is our main py file to run the game

import dice

def main():
    print("hello and welcome to our game. please roll the dice")
    x = 5
    test_die = dice.Dice()
    test_num = test_die.roll_the_dice()
    print(test_num)