""" Test player related stuffs """
import unittest

from blmsim import buffs
from blmsim.player import Player
from blmsim.targetdummy import TargetDummy
from blmsim.util.time import Clock

class TestPlayer(unittest.TestCase):

    def test_player_executing_fireIV(self):
        clock = Clock()
        player = Player('John', clock)
        player.receive_buff(buffs.EnochianBuff())
        dummy = TargetDummy()
        self.assertTrue(player.cast('Fire IV', dummy))
        self.assertFalse(player.cast('Fire IV', dummy))

    def test_player_casting_status(self):
        clock = Clock()
        player = Player('John', clock)
        dummy = TargetDummy()
        self.assertTrue(player.cast('Blizzard I', dummy))
        self.assertTrue(player.casting)
        tick_to_complete = Clock(player.skills['Blizzard I'].cast_time).ticks
        self.assertFalse(player.cast('Fire IV', dummy))
        for _ in range(tick_to_complete):
            clock.tick()
        clock.tick()
        self.assertFalse(player.casting)

    def test_player_use_swiftcast(self):
        clock = Clock()
        player = Player('John', clock)
        dummy = TargetDummy()
        self.assertTrue(player.cast('Swiftcast', player))
        self.assertTrue(player.casting)
        tick_to_complete = Clock(player.skills['Swiftcast'].cast_time).ticks
        self.assertEqual(len(player.buffs), 1)
        self.assertEqual(player.buffed['cast_time_multiplier'], 0)
        for _ in range(tick_to_complete):
            clock.tick()
        clock.tick()
        player.cast('Blizzard I', dummy)
        clock.tick()  # trigger cast Blizzard I
        self.assertFalse('Swiftcast' in player.buffs)
        self.assertNotEqual(player.buffed['cast_time_multiplier'], 0)

    def test_player_gcd(self):
        clock = Clock()
        player = Player('John', clock)
        dummy = TargetDummy()
        self.assertTrue(player.cast('Blizzard I', dummy))
        self.assertTrue(player.casting)
        tick_to_complete = Clock(player.skills['Blizzard I'].cast_time).ticks
        for _ in range(tick_to_complete):
            clock.tick()
        self.assertTrue(player.casting)
        clock.tick()
        self.assertFalse(player.casting)

    def test_player_enochian_validity(self):
        clock = Clock()
        player = Player('John', clock)
        player.receive_buff(buffs.AstralFireBuff(1))
        player.cast('Enochian', player)
        clock.tick()
        self.assertTrue('Enochian' in player.buffs)
        for _ in range(buffs.AstralFireBuff(1).duration.ticks):
            clock.tick()
        self.assertFalse('Astral Fire' in player.buffs)
        self.assertFalse('Enochian' in player.buffs)

    def test_player_foul_and_polyglot(self):
        clock = Clock()
        player = Player('John', clock)
        dummy = TargetDummy()
        player.receive_buff(buffs.AstralFireBuff(1))
        self.assertTrue(player.cast('Enochian', player))
        clock.tick()
        player.casting_time.set_time(0)
        self.assertTrue('Polyglot' in player.buffs)
        self.assertEqual(player.buffs['Polyglot'].charge, 0)
        self.assertFalse(player.cast('Foul', dummy))
        player.buffs['Polyglot'].gain_charge_timer.set_time(0)
        clock.tick()
        self.assertEqual(player.buffs['Polyglot'].charge, 1)
        self.assertTrue(player.cast('Foul', dummy))
        clock.tick()
        tick_to_complete = Clock(player.skills['Foul'].cast_time).ticks
        for _ in range(tick_to_complete):
            clock.tick()
        self.assertEqual(player.buffs['Polyglot'].charge, 0)
        self.assertTrue('Polyglot' in player.buffs)


if __name__ == '__main__':
    unittest.main()
