# In this code Each player should be able to select a name for themself.
# A player should be able to change their name.


def open_filewrite(list):
    with open('diceplayer1.txt', 'w') as f:
        f.write(list)
        f.close()


def open_fileread():
    result = ""
    try:
        with open('diceplayer1.txt', 'r') as f:
            result = f.read()
            print(result)
            f.close()

    except FileNotFoundError:
        with open('diceplayer1.txt', 'w') as f:
            f.close()

    return result


def create_player(list):
    name = input("Write your player name here: ")
    points = input(str("How many points: "))

    list = list + '\n' + name + ' : ' + points
    return list


def change_points():
    pass


def print_list(list):
    print(list)


def player_list():
    pass


def sort_highscore(highscore_list):
    print(highscore_list)
    split_list = highscore_list.splitlines()
    print(split_list)
    split_list.pop(0)
    print(split_list)
    new_split_list = split_list.splitlines()
    print(new_split_list)

    return split_list


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
        print("0: Exit")
        x = int(input("\nSelect option: "))
        match x:
            case 1:
                text_list = create_player(text_list)
            case 2:
                print_list(text_list)
            case 3:
                open_filewrite()
            case 4:
                open_fileread()
            case 5:
                open_filewrite(text_list)
            case 6:
                sort_highscore(text_list)


main()
