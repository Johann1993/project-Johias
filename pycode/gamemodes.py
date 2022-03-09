"""File contain the structure of the different gamemodes."""

import time
from typing import List
import dice
import bot_levels
import characters


def player_vs_bot():
    """
    For playing against a bot.

    it's created to keep the main class clean.
    """
    player_name = input(str("select player name: "))
    die_player1 = dice.Dice(player_name)
    die_computer = dice.Dice("Computer")
    game = bot_levels.BotDifficulty()

    while True:
        try:
            print("select difficulty.")
            choose_difficulty = int(input("1 for easy , 2 for medium: "))
            print(" ")
            if choose_difficulty > 2:
                print("bad input. select 1 or 2!")
            else:
                break
        except ValueError:
            print("only enter numbers!")

    while(die_player1.show_total() < 100 and die_computer.show_total() < 100):

        end_game = 0
        result = player_round(die_player1)
        die_player1.add_to_total(result)

        if result == 10001:
            print("you chose to exit game!")
            print("---------------------------")
            end_game = 1
            break
        else:
            if choose_difficulty == 1:
                total_points_computer = game.cpu_easy(die_computer)
                die_computer.add_to_total(total_points_computer)
                print("Computer now has a total of:")
                print(f"{die_computer.show_total()}")
                print("--------------------------------")
                time.sleep(1)
            elif choose_difficulty == 2:
                total_points_computer = game.cpu_medium(die_computer)
                die_computer.add_to_total(total_points_computer)
                print(f"computer total:{die_computer.show_total()}")
                print("--------------------------------")
                time.sleep(1)

    if end_game == 0:
        if (die_player1.show_total() > 100 and
            die_computer.show_total() > 100):
            print("It's a Tie! Both players lost!")
            print_rolles_endgame(die_player1, die_computer)

        elif die_computer.show_total() > 100:
            print("congratz! Computer actually won!")
            print_rolles_endgame(die_player1, die_computer)

        elif die_player1.show_total() > 100:
            print("Congratz! player won!")
            print_rolles_endgame(die_player1, die_computer)
            
        player1_score = [die_player1.get_name(), str(die_player1.show_total())]
        player2_score = [die_computer.get_name(), str(die_computer.show_total())]
        characters.open_filewrite(player1_score, player2_score)


def player_vs_player():
    """
    When selecting to play two players against each other.

    This method will run the gamemode.
    """
    player_name = input(str("select player name: "))
    player2_name = input(str("select player 2 name: "))
    print("----------------------")
    die_player1 = dice.Dice(player_name)
    die_player2 = dice.Dice(player2_name)

    while(die_player1.show_total() < 100 and die_player2.show_total() < 100):

        result = player_round(die_player1)
        die_player1.add_to_total(result)
        if result == 10001:
            print("Player 1 chose to exit game!")
            print("---------------------------")
            break

        result_player2 = player_round(die_player2)
        die_player2.add_to_total(result_player2)
        if result_player2 == 10001:
            print("Player 2 chose to exit game!")
            print("---------------------------")
            break

    if result != 10001 and result_player2 != 10001:
        if die_player1.show_total() > 100 and die_player2.show_total() > 100:
            print("it's a tie!")
            print_rolles_endgame_1vs1(die_player1, die_player2)
        elif die_player2.show_total() > 100:
            print(f"congratz! {die_player2.get_name()} actually won!")
            print_rolles_endgame_1vs1(die_player1, die_player2)
        elif die_player1.show_total() > 100:
            print(f"congratz! {die_player1.get_name()} actually won!")
            print_rolles_endgame_1vs1(die_player1, die_player2)

        player1_score = [die_player1.get_name(), str(result)]
        player2_score = [die_player2.get_name(), str(result_player2)]
        characters.open_filewrite(player1_score, player2_score)


def player_round(die_player):
    """
    Player function.

    This method contains the options for
    a players round and score counting
    """
    player_round_total = 0
    while True:
        print(" 1) Throw dice \n 2) End round \n 3) Use cheat")
        print(" 4) See rules \n 5) change dice highest value")
        print(" 6) Exit gamemode")
        selection = input(str(f"{die_player.get_name()} option: "))
        print(" ")
        match selection:
            case '1':
                diescore = die_player.roll_the_dice()
                if diescore >= 2:
                    print(f"{die_player.get_name()} rolled: {diescore}")
                    print(f"Round total:{diescore + player_round_total}")
                    print("------------------------------------")
                    player_round_total += diescore
                elif diescore == 1:
                    print("You rolled a 1, round total")
                    print("reset to 0. Other players turn!")
                    print("---------------------------")
                    player_round_total = 0
                    break
            case '2':
                die_player.add_to_total(player_round_total)
                player_round_total = 0
                print("you now have a total of :")
                print(f"{die_player.show_total()}")
                print("---------------------------------------")
                break
            case '3':
                diescore = die_player.roll_dice_cheat()
                print(f"you rolled a {diescore}! what are the odds!?")
                print("----------------------------------------")
                player_round_total += diescore
            case '4':
                see_rules()
            case '5':
                new_value = int(input("enter new highest value on the dice: "))
                die_player.change_highest_value(new_value)
            case '6':
                player_round_total = 10001
                break

    return player_round_total


def print_rolles_endgame(die_player, die_cpu):
    """Players as parameter.

    This function prints out the statistics of the game once finished.
    """
    print("You threw the dice")
    print(f"{die_player.show_amount_rolls()} times")
    print("Computer has thrown the dice")
    print(f"{die_cpu.show_amount_rolls()} times")


def print_rolles_endgame_1vs1(die_player, die_player2):
    """Players as parameter.

    This function prints out the statistics of the game once finished.
    """
    print(f"{die_player.get_name()} threw the dice")
    print(f"{die_player.show_amount_rolls()} times")
    print(f"{die_player2.get_name()} has thrown the dice")
    print(f"{die_player2.show_amount_rolls()} times")


def see_rules():
    """See the rules during the game."""
    print("""this is the rules to follow:
        first to reach a 100 points win.
        If you roll a 1, you loose all the points earned in that round.
        Should you choose to end your round your current points
        will be added to a total.
        Once you roll a 1 or choose to end your round,
        it's the opponents turn to roll.
        You should not but you could cheat by pressing
        4 when to throw the dice...""")
    print("----------------------------------------------------------\n")
