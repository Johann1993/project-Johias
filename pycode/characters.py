"""File save and sort players."""
# In this code Each player should be able to select a name for themself.
# A player should be able to change their name.


def open_filewrite(player1, player2):
    """Write player and points to file."""
    with open('PigHighscores.txt', 'a') as file:
        file.write(str(player1[0] + " : " + str(player1[1])) + "\n")
        file.write(str(player2[0] + " : " + str(player2[1])) + "\n")
        file.write("-----------\n")
        file.close()


def open_fileread():
    """Read player and points from file."""
    try:
        with open('PigHighscores.txt', 'r') as file:
            result = file.read()
    except FileNotFoundError:
        with open('PigHighscores.txt', 'w') as file:
            file.close()

    return result


def find_player(name, player_list):
    """Find player in textfile."""
    # Returns 0 if player not in list
    point = 0
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            point = player_list[i][1]

    return point


def delete_player(name, player_list):
    """Delete a player from list."""
    new_list = []
    for i in range(len(player_list)):
        if name != player_list[i][0]:
            new_list.append(player_list[i])

    return new_list


def update_points(name, points, player_list):
    """Update players points."""
    # Returns 0 if player not in list
    for i in range(len(player_list)):
        if name == player_list[i][0]:
            player_list[i][1] = points

    return player_list


def sort_highscore(highscore_list):
    """Sort player by highscore."""
    print(highscore_list)
    sorted_new_list = sorted(highscore_list, key=lambda x: x[1], reverse=True)
    print(sorted_new_list)

    return sorted_new_list
