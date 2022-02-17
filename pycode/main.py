# this is our main py file to run the game

import dice

def main():
    
    menu()
    
    test_die = dice.Dice()
    test_num = test_die.roll_the_dice()
    print(test_num)

def menu():
    print("""Welcome to the game! 
    below you will find your options! """)




if __name__ == '__main__':
    # Call the main function.
    main()