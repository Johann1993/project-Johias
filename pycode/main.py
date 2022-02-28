# this is our main py file to run the game
# . .venv/Scripts/activate     active venv in bash
import gamemodes


def main():

    menu()
    while True:
        options()
        x = input(str("select option: "))
        match x:
            case '1':
                gamemodes.player_vs_bot()
            case '2':
                gamemodes.Player_vs_Player()
            case '3':
                print("highscores will be shown here")
            case '4':
                gamemodes.see_rules()
            case '5':
                quit()


def menu():
    print("""
    Welcome to the game!
    This is the game pig!
    """)


def options():
    print("""This is your options:
    1) play game vs computer
    2) play game vs other player
    3) view local highscores
    4) view rules
    5) exit to desktop""")


def see_rules():
    print("""this is the rules to follow:
    first to reach a 100 points win.
    If you roll a 1, you loose all the points earned in that round.
    Should you choose to end your round your current points
    will be added to a total.
    Once you roll a 1 or choose to end your round, it's the
    opponents turn to roll.
    You should not but you could cheat by pressing 4 when to throw the dice...
    """)


def print_rolles_endgame(diePlayer, dieCpu):
    print(f"You threw the dice {diePlayer.show_amount_rolls()} times")
    print(f"Computer has thrown the dice:{dieCpu.show_amount_rolls()}")


if __name__ == '__main__':
    # Call the main function.
    main()
