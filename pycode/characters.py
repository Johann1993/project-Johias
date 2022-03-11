# In this code Each player should be able to select a name for themself. 
# A player should be able to change their name.

def open_filewrite(player1, player2):
    with open('PigHighscores.txt', 'a') as f:

        f.write(str(player1[0] + " : " + str(player1[1])) + "\n")
        f.write(str(player2[0] + " : " + str(player2[1])) + "\n")
        f.write("-----------\n")
        f.close()


def open_fileread():

    try:
        with open('PigHighscores.txt', 'r') as f:
            result = f.read()      
    except FileNotFoundError:
        with open('PigHighscores.txt', 'w') as f:
            f.close()

    return result


def find_player(name, player_list):
    # Returns 0 if player not in list
    point = 0
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            point = player_list[i][1]

    return point


def delete_player(name, player_list):
    """Deletes a player from list."""
    new_list = []
    for i in range(len(player_list)):
        if name != player_list[i][0]:
            new_list.append(player_list[i])

    return new_list


def update_points(name, points, player_list):
    # Returns 0 if player not in list
    #print(name + ' ' + str(points))
    #print(player_list)
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            player_list[i][1] = points


# Sort highscore list
def sort_highscore(highscore_list):

    print(highscore_list)
    sorted_new_list = sorted(highscore_list, key=lambda x: x[1], reverse=True)
    print(sorted_new_list)

    return sorted_new_list
