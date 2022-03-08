#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python file for running test on bots."""

import unittest
import bot_levels
import dice
from bot_levels import cpu_roll_one
from bot_levels import cpu_easy_roll_points
from bot_levels import cpu_medium_roll_points


class TestGamemodesClass(unittest.TestCase):
    """Testing bots.

    To ensure that the bots
    can generate points and operate as intended.
    """

    def test_bot_easy(self):
        """
        Creating a easy bot.

        Runs a round to see that it scores.
        """
        bot_test = dice.Dice()
        game = bot_levels.BotDifficulty()

        result = game.cpu_easy(bot_test)
        expected = 0 <= result <= 100
        self.assertTrue(expected)

    def test_bot_medium(self):
        """
        Creating a medium difficulty bot.

        Bot then runs a round to see if it works.
        """
        game = bot_levels.BotDifficulty()
        bot_test = dice.Dice()

        result = game.cpu_medium(bot_test)
        expected = 0 <= result <= 100
        self.assertTrue(expected)

    def test_easy_bot_several_rounds(self):
        """Easy bot running more rounds."""
        bot_test = dice.Dice()
        game = bot_levels.BotDifficulty()

        game_rounds = 0
        total_score = 0
        while game_rounds < 10:
            result = game.cpu_easy(bot_test)
            total_score += result
            game_rounds += 1

        expected = 0 <= total_score <= 100
        self.assertTrue(expected)

    def test_medium_bot_several_rounds(self):
        """Easy bot running more rounds."""
        bot_test = dice.Dice()
        game = bot_levels.BotDifficulty()

        game_rounds = 0
        total_score = 0
        while game_rounds < 10:
            result = game.cpu_medium(bot_test)
            total_score += result
            game_rounds += 1

        expected = 0 <= total_score <= 1000
        self.assertTrue(expected)

    def test_roll_one(self):
        """Test to make sure score is reset to 0."""
        expected = 0
        score = 20
        score = cpu_roll_one()
        self.assertEqual(expected, score)

    def test_easy_roll_points(self):
        """Test add points to easy bot."""
        expected = 10
        total_score = 5
        added_value = 5
        total_score = cpu_easy_roll_points(total_score, added_value)

        self.assertTrue(expected == total_score)

    def test_medium_roll_points(self):
        """Test add points to medium bot."""
        expected = 10
        total_score = 5
        added_value = 5
        total_score = cpu_medium_roll_points(total_score, added_value)

        self.assertTrue(expected == total_score)


if __name__ == "__main__":
    unittest.main()
