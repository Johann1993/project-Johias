from unicodedata import name
import unittest
import characters
import dice
import os.path


class TestCharactersClass(unittest.TestCase):
    """
    This class is for testing Characters.
    """
    def test_sort(self):
        """
        This test is testing the sort function.
        """
        die1 = dice.Dice("Fred")
        die2 = dice.Dice("John")

        die1.add_to_total(20)
        die2.add_to_total(50)

        new_list = [die1.get_name(), die1.show_total()]
        new_list2 = [die2.get_name(), die2.show_total()]
        next_list = [new_list, new_list2]

        sort_list = characters.sort_highscore(next_list)


        expected = "John"
        result = sort_list[0][0]

        self.assertEqual(expected, result)


    def test_find_player(self):
        """
        This test is testing if it can find a player
        """
        name = "John"
        points = 12
        player = [name, points]
        find = [player]
        result = characters.find_player(name, find)

        self.assertEqual(points, result)


    def test_delete(self):
        """ This test is testing the delete player????. """
        name = "John"
        points = 12
        name1 = "Tom"
        points1 = 43
        name2 = "Jake"
        points2 = 23

        player = [name, points]
        player1 = [name1, points1]
        player2 = [name2, points2]
        find = [player, player1, player2]
        new_list = characters.delete_player(name, find)

        self.assertNotEqual(find, new_list)


    def test_writefile(self):
        """ This test should test if the file gets open. """
        die1 = dice.Dice("Test")
        test = [die1.get_name(), str(die1.show_total())]
        characters.open_filewrite(test, test)
        file_exists = os.path.exists('PigHighscores.txt')

        self.assertTrue(file_exists)

    """
    def test_update(self):
        This test if points gets updated
        die1 = dice.Dice("Fred")
        die1.add_to_total(20)
        player = die1.get_name(), die1.show_total()
        expected = (('Fred', 30))

        self.assertNotEqual(expected, player)


    def test_openfile(self):
        This test will test so it is possible to open file
    """
        

if __name__ == '__main__':
    unittest.main()