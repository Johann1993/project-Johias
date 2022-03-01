"""
Python file containing messages and main function.

While running the program.
"""
# . .venv/Scripts/activate active venv in bash
import sys
import gamemodes


def main():
    """Where the complete program will be executed."""
    menu()
    while True:
        options()
        game_option = input(str("select option: "))
        match game_option:
            case '1':
                gamemodes.player_vs_bot()
            case '2':
                gamemodes.player_vs_player()
            case '3':
                print("highscores will be shown here")
            case '4':
                gamemodes.see_rules()
            case '5':
                sys.exit()


def menu():
    """Print function.

    Show statement when starting the game.
    """
    print("""
    Welcome to the game!
    This is the game pig.
    """)


def options():
    """See the options to select from."""
    print("""This is your options:
    1) play game vs computer
    2) play game vs other player
    3) view local highscores
    4) view rules
    5) exit to desktop""")


if __name__ == '__main__':
    # Call the main function.
    main()
