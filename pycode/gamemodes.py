"""File contain the structure of the different gamemodes."""

import time
import dice
import bot_levels


def player_vs_bot():
    """
    For playing against a bot.

    it's created to keep the main class clean.
    """
    die_player1 = dice.Dice()
    die_computer = dice.Dice()
    game = bot_levels.BotDifficulty()

    while True:
        try:
            choose_difficulty = int(input("""select difficulty.
            1 for easy , 2 for medium: """))
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
                print(f"""computer now has a total of:
                {die_computer.show_total()}""")
                print("--------------------------------")
                time.sleep(1)
            elif choose_difficulty == 2:
                total_points_computer = game.cpu_medium(die_computer)
                die_computer.add_to_total(total_points_computer)
                print(f"""computer now has a total of:
                {die_computer.show_total()}""")
                print("--------------------------------")
                time.sleep(1)

        if end_game == 0:
            if die_player1.show_total() > 100:
                print("congratz! Player actually won!")
                print_rolles_endgame(die_player1, die_computer)

            elif die_computer.show_total() > 100:
                print("congratz! Computer actually won!")
                print_rolles_endgame(die_player1, die_computer)

            elif(die_player1.show_total() > 100 and
                 die_computer.show_total() > 100):
                print("it's a tie!")
                print_rolles_endgame(die_player1, die_computer)


def player_vs_player():
    """
    When selecting to play two players against each other.

    This method will run the gamemode.
    """
    die_player1 = dice.Dice()
    die_player2 = dice.Dice()

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
        if die_player1.show_total() > 100:
            print("congratz! Player 1 actually won!")
            print_rolles_endgame_1vs1(die_player1, die_player2)
        elif die_player2.show_total() > 100:
            print("congratz! Computer actually won!")
            print_rolles_endgame_1vs1(die_player1, die_player2)
        elif die_player1.show_total() > 100 and die_player2.show_total() > 100:
            print("it's a tie!")
            print_rolles_endgame_1vs1(die_player1, die_player2)


def player_round(die_player):
    """
    Player function.

    This method contains the options for
    a players round and score counting
    """
    player_round_total = 0
    while True:
        selection = input(str(""" 1) To throw \n 2) End round \n 3) To cheat \n
        4) See rules \n 5) change dice highest value \n
        6) Exit gamemode \n Your option: """))
        print(" ")
        match selection:
            case '1':
                diescore = die_player.roll_the_dice()
                if diescore >= 2:
                    print(f"""your roll: {diescore}, added to your round total of:
                    {diescore + player_round_total},
                    Throw again or stop round?""")
                    print("""----------------------------------------------------
                    -----------------------------""")
                    player_round_total += diescore
                elif diescore == 1:
                    print("""You rolled a 1, round total
                    reset to 0. Other players turn!""")
                    print("""------------------------------
                    ------------------------------""")
                    player_round_total = 0
                    break

            case '2':
                die_player.add_to_total(player_round_total)
                print(f"""you now have a total of :
                {die_player.show_total()}""")
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
    print(f"""You threw the dice
    {die_player.show_amount_rolls()} times""")
    print(f"""Computer has thrown the dice
    {die_cpu.show_amount_rolls()} times""")


def print_rolles_endgame_1vs1(die_player, die_player2):
    """Players as parameter.

    This function prints out the statistics of the game once finished.
    """
    print(f"""You threw the dice
    {die_player.show_amount_rolls()} times""")
    print(f"""Player 2 has thrown the dice
    {die_player2.show_amount_rolls()} times""")


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
