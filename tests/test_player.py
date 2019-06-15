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

    def test_player_use_swiftcast(self):
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(player.cast('Swiftcast', player))
        self.assertTrue(player.casting)
        tick_to_complete = Clock(player.skills['Swiftcast'].cast_time).ticks
        self.assertEqual(len(player.buffs), 1)
        self.assertEqual(player.buffed['cast_time_multiplier'], 0)
        for i in range(tick_to_complete):
            clock.tick()
        clock.tick()
        player.cast('Blizzard I')
        clock.tick() # trigger cast Blizzard I
        self.assertEqual(len(player.buffs), 0)
        self.assertNotEqual(player.buffed['cast_time_multiplier'], 0)
        player.cast('Blizzard I')
        clock.tick()
        self.assertGreater(player.casting_time, Clock(0))


if __name__ == '__main__':
    unittest.main()
