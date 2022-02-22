# this is our main py file to run the game
# . .venv/Scripts/activate     active venv in bash


import dice
import random
import gamemodes


def main():

    menu()
    while True:
        options()
        x = input(str("select option: "))
        match x:
            case '1':
                print("test min spel class")
                die_playertob = dice.Dice()
                die_computer = dice.Dice()
                game = gamemodes.gamemode()

                while(die_playertob.show_total() < 100 and die_computer.show_total() < 100):
                    total_points = game.player_play()
                    print(f"{total_points}")
                    if(total_points == 10001):
                        break
                    die_playertob.add_to_total(total_points)
                    print("player now has a total of: " + str(die_playertob.show_total()))
                    print("-----------------")
                
                    total_points_computer = game.cpu_easy()
                    die_computer.add_to_total(total_points_computer)
                    print("computer now has a total of" + str(die_computer.show_total()))
                    print("------------------")

                    if(die_playertob.show_total() > 100):
                        print("congratz! Player actually won!")
                    elif(die_computer.show_total() > 100):
                        print("congratz! Computer actually won!")
             
            case '2':
                die_player1 = dice.Dice()
                die_player2 = dice.Dice()
                game = gamemodes.gamemode()

                while(die_player1.show_total() < 100 and die_player2.show_total() < 100):
                    total_points_p1 = game.player_play()
                    if(total_points_p1 == 10001):
                        break
                    die_player1.add_to_total(total_points_p1)
                    print("player 1 now has a total of: " + str(die_player1.show_total()))
                    print("-----------------")

                    total_points_p2 = game.player_play()
                    if(total_points_p2 == 10001):
                        break
                    die_player2.add_to_total(total_points_p2)
                    print("player 2 now has a total of: " + str(die_player2.show_total()))
                    print("-----------------")
            case '3':
                return 3
            case '4':
                print("skapa karaktär här ? ")
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
    3) watch computer play itself
    4) create character
    5) view local highscores""")

def look_rules():
    print("""this is the rules to follow:
    first to reach a 100 points win. 
    If you roll a 1, you loose all the point earned in that round.
    Should you choose to end your round your current points will be added to a total.
    Once you roll a 1, it's the opponents turn to roll. 
    You should not but you could cheat by pressing 4 when to throw the dice...
    """)

    

if __name__ == '__main__':
    # Call the main function.
    main()