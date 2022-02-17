# this is our main py file to run the game

import dice

def main():
    
    menu()

    options()
    x = input(str("select option "))
    match x:
        case '1':
            print("här kör vi gamemode 1")
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
            
                
    
    test_die = dice.Dice()
    test_num = test_die.roll_the_dice()
    print(test_num)

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