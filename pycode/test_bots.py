#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python file for running test on bots."""

import unittest
import bot_levels
import dice


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


if __name__ == "__main__":
    unittest.main()
