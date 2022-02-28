#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python file for running test on bots."""

import unittest
import botLevels
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
        botTest = dice.Dice()
        game = botLevels.botDifficulty()

        sum = game.cpu_easy(botTest)
        expected = 0 <= sum <= 100
        self.assertTrue(expected)

    def test_bot_medium(self):
        """
        Creating a medium difficulty bot.

        Bot then runs a round to see if it works.
        """
        game = botLevels.botDifficulty()
        botTest = dice.Dice()

        sum = game.cpu_medium(botTest)
        expected = 0 <= sum <= 100
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
