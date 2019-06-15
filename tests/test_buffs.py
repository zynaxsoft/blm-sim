import unittest
from blmsim.util.time import Clock, Time
from blmsim.skills import *
from blmsim.player import Player
from blmsim.buffs import *

class TestBuffs(unittest.TestCase):

    def test_buff_check_member_astral_umbral(self):
        a_list = [AstralFire(1), AstralFire(2), AstralFire(3)]
        u_list = [UmbralIce(1), UmbralIce(2), UmbralIce(3)]
        for i in range(1, 4):
            self.assertTrue(AstralFire(i) in a_list)
            self.assertFalse(AstralFire(i) in u_list)
            self.assertTrue(UmbralIce(i) in u_list)
            self.assertFalse(UmbralIce(i) in a_list)
        self.assertTrue('Astral or Umbral' in a_list)
        self.assertTrue('Astral or Umbral' in u_list)

if __name__ == '__main__':
    unittest.main()
