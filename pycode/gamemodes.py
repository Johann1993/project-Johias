# this is where all the gamemodes can be found

import dice
import random

class gamemode():

    def player_play(self):
        die_player = dice.Dice()
        player_total = 0

        while True:
            selection = input(str("1 to throw, 2 to exit, 3 to cheat, 4 to exit game"))
            match selection:
                case '1':
                    sum = die_player.roll_the_dice()
                    if (sum == 1):
                        print(" you rolled a one, round total set to 0. Other players turn!")
                        player_total = 0
                        break
                    elif (sum > 1):
                        print(f"you rolled a {sum}, added to your total. Throw again or stop round?")
                        player_total += sum
                case '2':
                    break
                case '3':
                    sum = die_player.roll_dice_cheat()
                    print(f"you rolled a {sum}! what are the odds!?")
                    player_total += sum
                case '4':
                    #exit game
                    print("you chose to exit game!")
                    player_total = 10001
                    break
        
        return player_total
        

    def cpu_easy(self):
        die_computer = dice.Dice()
        computer_total = 0

        while True:
            computer_selection = random.randint(1,2)
            match computer_selection:
                case 1:
                    sum = die_computer.roll_the_dice()
                    if (sum == 1):
                        print(" Computer rolled a one, round total set to 0. Other players turn!")
                        computer_total = 0
                        break
                    elif (sum > 1):
                        print(f"Computer rolled a {sum}, added to the round total.")
                        computer_total += sum
                case 2:
                    break

        return computer_total
                    

    def cpu_medium():
        die_computer_med = dice.Dice()
        computer_total = 0

        while True:
            sum = die_computer_med.roll_the_dice()
            if(sum == 1):
                print("Computer rolled a 1. round score set to 0")
                computer_total = 0
                break
            elif (sum > 1):
                if(computer_total > 10 and die_computer_med.my_rolls_amount > 3):
                    computer_total += sum
                    break
                else:
                    computer_total += sum

        return computer_total
