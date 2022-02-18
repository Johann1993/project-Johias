# this is where all the gamemodes can be found

import dice

class gamemode():

    def player_vs_computer(self):
        die_computer = dice.Dice()
        die_player1 = dice.Dice()
        print("You will go first! enter to hit dice or hold!")
        selection = input(str())
        while (selection != '3'):
            match selection:
                case '1':     # roll dice
                    sum = die_player1.roll_the_dice
                    print(sum)
                    selection = input(str())
        



    def player_vs_player():
        return 1

    def cpu_vs_cpu():
        return 3