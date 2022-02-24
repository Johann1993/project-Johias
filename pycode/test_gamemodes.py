#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import gamemodes
import dice

class TestGamemodesClass(unittest.TestCase):

    def test_player_play(self):
        game = gamemodes.gamemode()



    def test_bot_easy(self):
        game = gamemodes.gamemode()

        sum = game.cpu_easy()
        expected = 0 <= sum <= 100
        self.assertTrue(expected)

    def test_bot_medium(self):
        game = gamemodes.gamemode()

        sum = game.cpu_medium()
        expected = 0 <= sum <= 100
        self.assertTrue(expected)


