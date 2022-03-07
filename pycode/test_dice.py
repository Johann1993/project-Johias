#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""File for dice class tests."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """
    Class for testing Dice.

    Contains functions for testing
    the dice object.
    """

    def test_default_object(self):
        """
        Check object.

        Makes sure that an object is generated
        and that max score is a 6.
        """
        die = dice.Dice()

        self.assertIsInstance(die, dice.Dice)

        result = die.max_amount
        expected = 6

        self.assertEqual(result, expected)

    def test_roll_die(self):
        """
        Check number range.

        Rolling the dice should
        return a number between 1 and 6.
        """
        die = dice.Dice()

        result = die.roll_the_dice()
        expected = 1 <= result <= die.max_amount
        self.assertTrue(expected)

    def test_die_cheat(self):
        """Check dice cheat returns highest possible value."""
        die = dice.Dice()

        cheat_res = die.roll_dice_cheat()
        expected = 6
        self.assertEqual(cheat_res, expected)

    def test_show_total(self):
        """Check that starting score of dice is 0."""
        die = dice.Dice()

        result = die.show_total()
        expected = 0

        self.assertEqual(result, expected)

    def test_add_sum(self):
        """Check if adding scores to total game points works."""
        die = dice.Dice()

        die.add_to_total(5)
        result = die.show_total()
        expected_sum = 5
        self.assertEqual(result, expected_sum)

    def test_change_dice_value(self):
        """Test to change highest dice roll value."""
        die = dice.Dice()

        start_value = die.roll_dice_cheat()
        die.change_highest_value(20)
        new_value = die.roll_dice_cheat()

        self.assertNotEqual(start_value, new_value)

    def test_show_number_rolls(self):
        """Test to retrieve number of rolls."""

        die = dice.Dice()

        expected = 4
        rolls = 0
        while rolls <= 3:
            die.roll_the_dice()
            rolls += 1

        total_rolls = die.show_amount_rolls()

        self.assertEqual(total_rolls, expected)


if __name__ == "__main__":
    unittest.main()
