#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import botLevels
import dice


class TestGamemodesClass(unittest.TestCase):

    def test_bot_easy(self):
        botTest = dice.Dice()
        game = botLevels.botDifficulty()

        sum = game.cpu_easy(botTest)
        expected = 0 <= sum <= 100
        self.assertTrue(expected)

    def test_bot_medium(self):
        game = botLevels.botDifficulty()
        botTest = dice.Dice()

        sum = game.cpu_medium(botTest)
        expected = 0 <= sum <= 100
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
