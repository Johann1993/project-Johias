"""Python file for AI bots."""
import time
import random


class BotDifficulty():
    """This class contains the AI for how the bots operates."""

    def cpu_easy(self, die_computer):
        """
        Contains a easy-level AI.

        To play against, with a dice object as
        parameter and that returns a round score.
        """
        computer_total = 0

        while True:
            computer_selection = random.randint(1, 2)
            match computer_selection:
                case 1:
                    result = die_computer.roll_the_dice()
                    if result > 1:
                        print(f"""Computer rolled a
                        {result}, added to the round total.""")
                        computer_total += result
                        time.sleep(2)
                    elif result == 1:
                        print("""Computer rolled a 1,
                        round total set to 0. Other players turn!""")
                        computer_total = 0
                        break
                case 2:
                    print("computer chose to stop round!")
                    break

        return computer_total

    def cpu_medium(self, die_computer):
        """
        Contains a medium-level AI.

        To play against, with a dice object as parameter
        and that returns a rounds score.
        """
        computer_total = 0

        while True:
            result = die_computer.roll_the_dice()
            if result >= 2:
                print(f"Computer rolled a {result}")
                time.sleep(2)
                if (computer_total == 12 and
                    die_computer.my_rolls_amount == 2):
                    print("computer chose to stop round!")
                    computer_total += result
                    break
                elif computer_total > 15 and die_computer.my_rolls_amount >= 3:
                    print("computer chose to stop round!")
                    computer_total += result
                    break
                else:
                    computer_total += result
            elif result == 1:
                print("Computer rolled a 1. round score set to 0")
                computer_total = 0
                break

        return computer_total
