#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import botLevels
import dice

class TestGamemodesClass(unittest.TestCase):

    def test_bot_easy(self):
        game = botLevels.botDifficulty()

        sum = game.cpu_easy()
        expected = 0 <= sum <= 100
        self.assertTrue(expected)

    def test_bot_medium(self):
        game = botLevels.botDifficulty()

        sum = game.cpu_medium()
        expected = 0 <= sum <= 100
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
