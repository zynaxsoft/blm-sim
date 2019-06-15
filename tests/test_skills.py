import unittest
from blmsim.util.time import Clock, Time
from blmsim.skills import *
from blmsim.player import Player

class TestSkills(unittest.TestCase):

    def test_skill_gcd(self):
        gcd_clock = Clock(default=2.5)
        gcd_skill = GCD('FIRE TEN', gcd_clock, cast_time=2.8)
        gcd_clock.set_time(1)
        self.assertFalse(gcd_skill.execute(None))
        gcd_clock.set_time(0)
        self.assertTrue(gcd_skill.execute(None))
        self.assertEqual(gcd_clock, Clock(2.5))

    def test_skill_ogcd(self):
        skill = OGCD('OGCD', cooldown=5)
        self.assertTrue(skill.execute(None))
        self.assertFalse(skill.execute(None))
        skill.clock.set_time(0)
        self.assertTrue(skill.execute(None))

    def test_skill_ley_line(self):
        skill = LeyLine()
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(skill.execute(player))
        self.assertFalse(skill.execute(player))
        self.assertNotEqual(player.buffed['cast_time_multiplier'], 1)
        self.assertNotEqual(player.buffed['gcd'], player.base['gcd'])

    def test_skill_swiftcast(self):
        skill = Swiftcast()
        clock = Clock()
        player = Player('John', clock)
        self.assertTrue(skill.execute(player))
        self.assertFalse(skill.execute(player))
        self.assertEqual(player.buffed['cast_time_multiplier'], 0)
        self.assertEqual(player.buffed['gcd'], player.base['gcd'])

if __name__ == '__main__':
    unittest.main()
