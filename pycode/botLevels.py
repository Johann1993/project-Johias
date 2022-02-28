

import time
import random


class botDifficulty():

    def cpu_easy(self, die_computer):
        computer_total = 0

        while True:
            computer_selection = random.randint(1, 2)
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

    def cpu_medium(self, die_computer):
        computer_total = 0

        while True:
            sum = die_computer.roll_the_dice()
            if(sum == 1):
                print("Computer rolled a 1. round score set to 0")
                computer_total = 0
                break
            elif (sum > 1):
                print(f"Computer rolled a {sum}")
                time.sleep(2)
                if(computer_total > 10 and die_computer.my_rolls_amount >= 3):
                    print("computer chose to stop round!")
                    computer_total += sum
                    break
                elif(computer_total > 12 and die_computer.my_rolls_amount == 2):
                    print("computer chose to stop round!")
                    computer_total += sum
                    break
                else:
                    computer_total += sum

        return computer_total
