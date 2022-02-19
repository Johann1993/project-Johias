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
            while (die_player1.total_amount < 100 or die_computer.total_amount < 100):
                while True:
                    selection = int(input("1 to throw, 2 to stop"))
                    if (selection == 1):
                        sum = die_player1.roll_the_dice()
                        print(f"you rolled a {sum}")
                        if (sum == 1):
                            player1_total = 0
                            print("round score set to 0. Computers turn")
                            print("-------------------------------------")
                            break
                        elif(sum > 1):
                            player1_total += sum
                            print("you now have " + str(player1_total)+  " in this round")
                            print("and in total you have "+ str(die_player1.total_amount))
                            print("------------------------------------")
                    elif (selection == 2):
                        die_player1.add_to_total(player1_total)
                        player1_total = 0
                        print("Computers turn!")
                        break
                    elif (selection == 3):
                        print("you chose to exit game!")
                        break
                    elif(selection == 4):
                        sum = die_player1.roll_dice_cheat()
                        print(f"you got a {sum}. wow, what are the odds!?")
                        player1_total += sum
                        print(f"round total: {player1_total}")

                
                while True:
                    computer_selection = random.randint(1,2)
                    if(computer_selection == 1):
                        sum_comp = die_computer.roll_the_dice()
                        print(f"computer rolled a {sum_comp}")
                        if(sum_comp > 1):
                            computer_total += sum_comp
                            print(f"computer now has a total of {computer_total} this round")
                        elif(sum_comp == 1):
                            computer_total = 0
                            print("total round score set to zero. player 1 turn again")
                            break
                    elif(computer_selection == 2):
                        print("computer gave up this round. pathetic")
                        break
               
                
                    

                
        case '2':
            print("Player vs Player")
        case '3':
            print("Highscores(local)")
        case '4':
            print("skapa karaktär här ? ")

            


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