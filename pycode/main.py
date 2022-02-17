# this is our main py file to run the game

import dice

def main():
    
    menu()

    x = input(str("select option "))
    match x:
        case '1':
            print("test case 1")
        case '2':
            print("test case 2")
            
                
    
    test_die = dice.Dice()
    test_num = test_die.roll_the_dice()
    print(test_num)

def menu():
    print(""" 
    Welcome to the game! 
    below you will find your options!
    
    1) create character
    2) view highscores
    3) play against computer
    4) play 1v1 
    5) watch computer play against itself """)

    




if __name__ == '__main__':
    # Call the main function.
    main()