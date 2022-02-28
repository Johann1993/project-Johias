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

        cheatRes = die.roll_dice_cheat()
        expected = 6
        self.assertEqual(cheatRes, expected)

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
        sum = die.show_total()
        expected_sum = 5
        self.assertEqual(sum, expected_sum)


if __name__ == "__main__":
    unittest.main()
