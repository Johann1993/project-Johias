# this is our main py file to run the game
# . .venv/Scripts/activate     active venv in bash


import dice
import random

def main():

    
    
    menu()

    options()
    x = input(str("select option "))
    match x:
        case '1':
            die_player1 = dice.Dice()
            die_computer = dice.Dice()
            player1_total = 0
            computer_total = 0
            while (die_player1.total_amount or die_computer.total_amount < 100):
                selection = input(str("1 to throw, 2 to stop"))
                if (selection == '1'):
                    sum = die_player1.roll_the_dice()
                    print(f"you rolled a {sum}, continue playing? 1 for yes, 2 to stop")
                    if (sum == 1):
                        player1_total = 0
                        print("round score set to 0. Computers turn")
                    elif(sum > 0):
                        player1_total += sum
                        print("you now have " + str(player1_total)+  " in this round")
                        print("and in total you have "+ str(die_player1.total_amount))
                elif (selection == '2'):
                    die_player1.add_to_total(player1_total)
                    print("Computers turn!")
                    
                
        case '2':
            print("gamemode 2")
        case '3':
            print("gamemode 3")
        case '4':
            print("skapa karaktär här ? ")
        case '5':
            print("kolla highscore här ? ")
        case '6':
            print("hej johan!")
            


def menu():
    print(""" 
    Welcome to the game! 
    This is the game pig!
    The rules are : you will throw the dice and the amount will be added to your total.
    If the dice stops on 1, you total amount for the round will be set to 0
    first to 100 points win!
    no cheating! (except with command "i am a cheat")
    """)

def options():
    print("""This is your options:
    1) play game vs computer
    2)play game vs other player
    3) watch computer play itself
    4) create character
    5) view local highscores""")

    

if __name__ == '__main__':
    # Call the main function.
    main()