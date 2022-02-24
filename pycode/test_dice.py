#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import dice


class TestDiceClass(unittest.TestCase):

    def test_default_object(self):
        #create an object and check values true or not
        die = dice.Dice()

        self.assertIsInstance(die, dice.Dice)

        result = die.max_amount
        expected = 6

        self.assertEqual(result, expected)

    def test_roll_die(self):
        die = dice.Dice()

        result = die.roll_the_dice()
        expected = 1 <= result <= die.max_amount
        self.assertTrue(expected)

    def test_die_cheat(self):
        die = dice.Dice()

        cheatRes = die.roll_dice_cheat()
        expected = 6
        self.assertEqual(cheatRes, expected)

    def test_show_total(self):
        die = dice.Dice()

        result = die.show_total()
        expected = 0

        self.assertEqual(result, expected)

    def test_add_sum(self):
        die = dice.Dice()

        die.add_to_total(5)
        sum = die.show_total()
        expected_sum = 5
        self.assertEqual(sum, expected_sum)

if __name__ == "__main__":
    unittest.main()

