import unittest
from blmsim.util.time import Clock, Time
from blmsim.skills import *
from blmsim.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_executing_fireIV(self):
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(player.cast('Fire IV'))
        self.assertFalse(player.cast('Fire IV'))

    def test_player_casting_status(self):
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(player.cast('Fire IV'))
        self.assertTrue(player.casting)
        tick_to_complete = Clock(player.skills['Fire IV'].cast_time).ticks
        for i in range(tick_to_complete):
            clock.tick()
            self.assertFalse(player.cast('Fire IV'))
        clock.tick()
        self.assertFalse(player.casting)

if __name__ == '__main__':
    unittest.main()
