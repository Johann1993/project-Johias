# this is where all the gamemodes can be found

import dice
import random
import time


class gamemode():

    def player_play(self):
        die_player = dice.Dice()
        player_total = 0

        while True:
            try:
                selection = input(str(" 1) to throw \n 2) end round \n 3) to cheat \n 4) to exit game \n 5) to see rules again \n your option: "))
                print(" ")
                match selection:
                    case '1':
                        sum = die_player.roll_the_dice()
                        if (sum == 1):
                            print(" you rolled a 1, round total reset to 0. Other players turn!")
                            print("------------------------------------------------------------")
                            player_total = 0
                            break
                        elif (sum > 1):
                            print(f"your roll: {sum}, added to your round total of: {sum + player_total}, Throw again or stop round?")
                            print("---------------------------------------------------------------------------------")
                            player_total += sum
                    case '2':
                        break
                    case '3':
                        sum = die_player.roll_dice_cheat()
                        print(f"you rolled a {sum}! what are the odds!?")
                        print("----------------------------------------")
                        player_total += sum
                    case '4':
                        #exit game
                        print("you chose to exit game!")
                        print("---------------------------")
                        player_total = 10001
                        break
                    case '5':
                        gamemode.see_rules()
            except TypeError:
                print("pressed invalid key!")
        
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
                        print(" Computer rolled a 1, round total set to 0. Other players turn!")
                        computer_total = 0
                        break
                    elif (sum > 1):
                        print(f"Computer rolled a {sum}, added to the round total.")
                        computer_total += sum
                        time.sleep(2)
                case 2:
                    print("computer chose to stop round!")
                    break

        return computer_total
                    

    def cpu_medium(self):
        die_computer_med = dice.Dice()
        computer_total = 0

        while True:
            sum = die_computer_med.roll_the_dice()
            if(sum == 1):
                print("Computer rolled a 1. round score set to 0")
                computer_total = 0
                break
            elif (sum > 1):
                print(f"Computer rolled a {sum}")
                time.sleep(2)
                if(computer_total > 10 and die_computer_med.my_rolls_amount >= 3):
                    print("computer chose to stop round!")
                    computer_total += sum
                    break
                elif(computer_total > 12 and die_computer_med.my_rolls_amount == 2):
                    print("computer chose to stop round!")
                    computer_total += sum
                    break
                else:
                    computer_total += sum
                    

        return computer_total


    def see_rules():
        print("""this is the rules to follow:
        first to reach a 100 points win. 
        If you roll a 1, you loose all the points earned in that round.
        Should you choose to end your round your current points will be added to a total.
        Once you roll a 1 or choose to end your round, it's the opponents turn to roll. 
        You should not but you could cheat by pressing 4 when to throw the dice...
        """)