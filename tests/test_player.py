import unittest
from blmsim.util.time import Clock, Time
from blmsim.skills import *
from blmsim.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_executing_fireIV(self):
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(player.cast('FireIV'))
        self.assertFalse(player.cast('FireIV'))

if __name__ == '__main__':
    unittest.main()
