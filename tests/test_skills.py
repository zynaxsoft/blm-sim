import unittest
from blmsim.util.time import Clock, Time
from blmsim.skills import *

class TestSkills(unittest.TestCase):

    def test_gcd(self):
        gcd_clock = Clock(default=2.5)
        gcd_skill = GCD('FIRE TEN', gcd_clock, 2.8)
        gcd_clock.set_time(1)
        self.assertFalse(gcd_skill.execute())
        gcd_clock.set_time(0)
        self.assertTrue(gcd_skill.execute())
        self.assertEqual(gcd_clock, Clock(2.5))

if __name__ == '__main__':
    unittest.main()
