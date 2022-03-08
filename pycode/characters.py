# In this code Each player should be able to select a name for themself. 
# A player should be able to change their name.

def open_filewrite(list_of_players):
    list = ''
    with open('diceplayer1.txt', 'w') as f:

        for i in range(len(list_of_players)):
            list = list + list_of_players[i][0] + ':' + str(list_of_players[i][1]) + '\n'

        print(list)

        f.write(list)
        f.close()


def open_fileread():
    result = ""
    new_list = []
    try:
        with open('diceplayer1.txt', 'r') as f:
            result = f.read()
            print(result)
            split_list = result.splitlines()
            print(split_list)
            print(len(split_list))

            for i in range(len(split_list)):
                print(split_list[i])
                p_list = split_list[i].split(':')
                p_list[1] = int(p_list[1])
                new_list.append(p_list)

            print(new_list)

    except FileNotFoundError:
        with open('diceplayer1.txt', 'w') as f:
            f.close()

    return new_list


def create_player(list):
    new_player = []
    name = input("Write your player name here: ")
    points = input(str("How many points: "))
    points2 = int(points)
    new_player.append(name)
    new_player.append(points2)
    list.append(new_player)
    return list


def print_list(list):
    print(list)


def change_name(name, player_list):
    print(name)
    print(player_list)
    new_name = input("Whats your new name? ")
    print(name + " your new name will be " + new_name)
    point = 0
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            player_list[i][0] = new_name

    return point


def find_player(name, player_list):
    # Returns 0 if player not in list
    print(name)
    print(player_list)
    point = 0
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            point = player_list[i][1]

    return point


def delete_player(name, player_list):
    # Returns 0 if player not in list
    print(name)
    print(player_list)
    point = 0
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            point = player_list[i][1]
            player_list.remove(player_list[i])
            return point

    return point


def update_points(name, points, player_list):
    # Returns 0 if player not in list
    print(name + ' ' + str(points))
    print(player_list)
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            player_list[i][1] = points


# Sort highscore list
def sort_highscore(highscore_list):

    print(highscore_list)
    sorted_new_list = sorted(highscore_list, key=lambda x: x[1], reverse=True)
    print(sorted_new_list)

    return sorted_new_list


def main():

    text_list = open_fileread()

    x = ''
    while x != 0:
        print("")
        print("1: Create player")
        print("2: Highscore")
        print("3: Clean highscore")
        print("4: Find player")
        print("5: Save highscore")
        print("6: Sort highscore")
        print("7: Delete player")
        print("8: Update player points")
        print("9: Change name")
        print("0: Exit")
        try:
            x = int(input("\nSelect option: "))
            match x:
                case 1:
                    text_list = create_player(text_list)
                case 2:
                    print_list(text_list)
                case 3:
                    open_filewrite()
                case 4:
                    name = input("Write player name here: ")
                    player_points = find_player(name, text_list)
                    if player_points != 0:
                        print('Player ' + name + ' excist in list' 
                              + '\nPoints = ' + str(player_points))
                    else:
                        print('Player ' + name + ' don´t exsist')
                case 5:
                    open_filewrite(text_list)
                case 6:
                    text_list = sort_highscore(text_list)
                case 7:
                    name = input("Write player name here: ")
                    player_points = delete_player(name, text_list)
                    if player_points != 0:
                        print('Player ' + name + ' deleted')
                case 8:
                    name = input("Write player name here: ")
                    player_points = find_player(name, text_list)
                    if player_points != 0:
                        points = input(str("How many points: "))
                        points2 = int(points)
                        update_points(name, points2, text_list)
                    else:
                        print('Player ' + name + ' don´t exsist')
                case 9:
                    name = input("Write player name here: ")
                    player_points = change_name(name, text_list)
        except ValueError:
            print('Oups, that was not the correct format. Try again!')


main()
