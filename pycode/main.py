"""
Python file containing messages and main function.

While running the program.
"""
# . .venv/Scripts/activate active venv in bash
import sys
import gamemodes
import characters


def main():
    """Where the complete program will be executed."""
    menu()
    while True:
        options()
        game_option = input(str("select option: "))
        print("-------------------")
        match game_option:
            case '1':
                gamemodes.player_vs_bot()
            case '2':
                gamemodes.player_vs_player()
            case '3':
                print("highscores:")
                highscores = characters.open_fileread()
                print(highscores)
            case '4':
                gamemodes.see_rules()
            case '5':
                sys.exit()


def menu():
    """Print function.

    Show statement when starting the game.
    """
    print('''
    Welcome to the game.
    This is the game pig!
    ''')


def options():
    """See the options to select from."""
    print("This is your options:")
    print("1) play game vs computer")
    print("2) play game vs other player")
    print("3) view local highscores")
    print("4) view rules")
    print("5) exit to desktop")


if __name__ == '__main__':
    # Call the main function.
    main()
