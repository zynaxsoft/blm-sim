""" Test usage of skills """
import unittest

from blmsim import skills, skillmeta
from blmsim.player import Player
from blmsim.targetdummy import TargetDummy
from blmsim.util.time import Clock

class TestSkills(unittest.TestCase):

    def test_skill_gcd(self):
        gcd_clock = Clock(default=2.5)
        gcd_skill = skillmeta.GCD('FIRE TEN', gcd_clock, cast_time=2.8)
        gcd_clock.set_time(1)
        self.assertFalse(gcd_skill.execute(None, None))
        gcd_clock.set_time(0)
        self.assertTrue(gcd_skill.execute(None, None))
        self.assertEqual(gcd_clock, Clock(2.5))

    def test_skill_ogcd(self):
        skill = skillmeta.OGCD('OGCD', cooldown=5)
        self.assertTrue(skill.execute(None, None))
        self.assertFalse(skill.execute(None, None))
        skill.clock.set_time(0)
        self.assertTrue(skill.execute(None, None))

    def test_skill_ley_line(self):
        skill = skills.LeyLine()
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(skill.execute(player, player))
        self.assertFalse(skill.execute(player, player))
        self.assertNotEqual(player.buffed['cast_time_multiplier'], 1)
        self.assertNotEqual(player.buffed['gcd'], player.base['gcd'])

    def test_skill_swiftcast(self):
        skill = skills.Swiftcast()
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(skill.execute(player, player))
        self.assertFalse(skill.execute(player, player))
        self.assertEqual(player.buffed['cast_time_multiplier'], 0)
        self.assertEqual(player.buffed['gcd'], player.base['gcd'])

    def test_skill_apply_buff_after_gcd_casted(self):
        clock = Clock()
        player = Player('John', clock)
        dummy = TargetDummy()
        player.cast('Blizzard I', dummy)
        tick_to_complete = Clock(player.skills['Blizzard I'].cast_time).ticks
        for _ in range(tick_to_complete):
            clock.tick()
            self.assertFalse('Umbral Ice' in player.buffs)
        clock.tick()
        self.assertTrue('Umbral Ice' in player.buffs)

if __name__ == '__main__':
    unittest.main()
