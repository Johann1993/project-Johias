# this is where all the gamemodes can be found


import dice
import botLevels
import time

#class gamemode():

def player_vs_bot():
        # **gamemode player VS computer**
        die_player1 = dice.Dice()
        die_computer = dice.Dice()
        game = botLevels.botDifficulty()

        while True:
            try:
                choose_difficulty = int(input("select difficulty. 1 for easy , 2 for medium: "))
                print(" ")
                if(choose_difficulty > 2):
                    print("bad input. select 1 or 2!")
                else:
                    break
            except:
                print("only enter numbers!")

        while(die_player1.show_total() < 100 and die_computer.show_total() < 100):
            playerRoundTotal = 0
            endgame = 0
            while True:
                selection = input(str(" 1) To throw \n 2) End round \n 3) To cheat \n 4) See rules \n 5) Exit gamemode \n Your option: "))
                print(" ")
                match selection:
                    case '1':
                        diescore = die_player1.roll_the_dice()
                        if(diescore == 1):
                            print(" you rolled a 1, round total reset to 0. Other players turn!")
                            print("------------------------------------------------------------")
                            playerRoundTotal = 0
                            break
                        elif(diescore >= 2):
                            print(f"your roll: {diescore}, added to your round total of: {diescore + playerRoundTotal}, Throw again or stop round?")
                            print("---------------------------------------------------------------------------------")
                            playerRoundTotal += diescore

                    case '2':
                        die_player1.add_to_total(playerRoundTotal)
                        print(f"you now have a total of :{die_player1.show_total()}")
                        print("---------------------------------------")
                        break
                    case '3':
                        diescore = die_player1.roll_dice_cheat()
                        print(f"you rolled a {diescore}! what are the odds!?")
                        print("----------------------------------------")
                        playerRoundTotal += diescore
                    case '4':
                        see_rules()
                    case '5':
                        break

            if(selection == '5'):
                print("you chose to exit game!")
                print("---------------------------")
                endgame = 1
                break

            if(endgame == 0):    
                if(choose_difficulty == 1):
                    total_points_computer = game.cpu_easy(die_computer)
                    die_computer.add_to_total(total_points_computer)
                    print(f"computer now has a total of: {die_computer.show_total()}")
                    print("--------------------------------")
                    time.sleep(2)
                elif(choose_difficulty == 2):
                    total_points_computer = game.cpu_medium(die_computer)
                    die_computer.add_to_total(total_points_computer)
                    print(f"computer now has a total of: {die_computer.show_total()}")
                    print("--------------------------------")
                    time.sleep(2)


            if(endgame == 0):
                if(die_player1.show_total() > 100):
                    print("congratz! Player actually won!")
                    print_rolles_endgame(die_player1,die_computer)

                elif(die_computer.show_total() > 100):
                    print("congratz! Computer actually won!")
                    print_rolles_endgame(die_player1,die_computer)

                elif(die_player1.show_total() > 100 and die_computer.show_total() > 100):
                    print("it's a tie!")
                    print_rolles_endgame(die_player1,die_computer)



def Player_vs_Player():
    # gamemode player VS player
    die_player1 = dice.Dice()
    die_player2 = dice.Dice()
    
    while(die_player1.show_total() < 100 and die_player2.show_total() < 100):
        playerRoundTotal = 0
        player2RoundTotal = 0
        while True:
            selection = input(str(" 1) To throw \n 2) End round \n 3) To cheat \n 4) See rules \n 5) Exit gamemode \n Your option: "))
            print(" ")
            match selection:
                case '1':
                    diescore = die_player1.roll_the_dice()
                    if(diescore == 1):
                        print(" you rolled a 1, round total reset to 0. Other players turn!")
                        print("------------------------------------------------------------")
                        playerRoundTotal = 0
                        break
                    elif(diescore >= 2):
                        print(f"your roll: {diescore}, added to your round total of: {diescore + playerRoundTotal}, Throw again or stop round?")
                        print("---------------------------------------------------------------------------------")
                        playerRoundTotal += diescore

                case '2':
                    die_player1.add_to_total(playerRoundTotal)
                    print(f"you now have a total of :{die_player1.show_total()}")
                    print("---------------------------------------")
                    break
                case '3':
                    diescore = die_player1.roll_dice_cheat()
                    print(f"you rolled a {diescore}! what are the odds!?")
                    print("----------------------------------------")
                    playerRoundTotal += diescore
                case '4':
                    see_rules()
                case '5':
                    break
        
        while True:
            selection = input(str(" 1) To throw \n 2) End round \n 3) To cheat \n 4) See rules \n 5) Exit gamemode \n Your option: "))
            print(" ")
            match selection:
                case '1':
                    diescore = die_player2.roll_the_dice()
                    if(diescore == 1):
                        print(" you rolled a 1, round total reset to 0. Other players turn!")
                        print("------------------------------------------------------------")
                        playerRoundTotal = 0
                        break
                    elif(diescore >= 2):
                        print(f"your roll: {diescore}, added to your round total of: {diescore + player2RoundTotal}, Throw again or stop round?")
                        print("---------------------------------------------------------------------------------")
                        player2RoundTotal += diescore

                case '2':
                    die_player2.add_to_total(player2RoundTotal)
                    print(f"you now have a total of :{die_player2.show_total()}")
                    print("---------------------------------------")
                    break
                case '3':
                    diescore = die_player2.roll_dice_cheat()
                    print(f"you rolled a {diescore}! what are the odds!?")
                    print("----------------------------------------")
                    player2RoundTotal += diescore
                case '4':
                    see_rules()
                case '5':
                    break

    if(die_player1.show_total() > 100):
        print("congratz! Player 1 actually won!")
        print_rolles_endgame_1vs1(die_player1,die_player2)
    elif(die_player2.show_total() > 100):
        print("congratz! Computer actually won!")
        print_rolles_endgame_1vs1(die_player1,die_player2)
    elif(die_player1.show_total() > 100 and die_player2.show_total() > 100):
        print("it's a tie!")
        print_rolles_endgame_1vs1(die_player1,die_player2)

        


def print_rolles_endgame(diePlayer,dieCpu):
        print(f"You threw the dice {diePlayer.show_amount_rolls()} times")
        print(f"Computer has thrown the dice {dieCpu.show_amount_rolls()} times")

def print_rolles_endgame_1vs1(diePlayer,dieplayer2):
        print(f"You threw the dice {diePlayer.show_amount_rolls()} times")
        print(f"Player 2 has thrown the dice {dieplayer2.show_amount_rolls()} times")


def see_rules():
        print("""this is the rules to follow:
        first to reach a 100 points win. 
        If you roll a 1, you loose all the points earned in that round.
        Should you choose to end your round your current points will be added to a total.
        Once you roll a 1 or choose to end your round, it's the opponents turn to roll. 
        You should not but you could cheat by pressing 4 when to throw the dice...
        """)
    