""" Test buff related """
import unittest

from blmsim import buffs

class TestBuffs(unittest.TestCase):

    def test_buff_check_member_astral_umbral(self):
        a_list = [buffs.AstralFire(1),
                  buffs.AstralFire(2),
                  buffs.AstralFire(3)]
        u_list = [buffs.UmbralIce(1),
                  buffs.UmbralIce(2),
                  buffs.UmbralIce(3)]
        for i in range(1, 4):
            self.assertTrue(buffs.AstralFire(i) in a_list)
            self.assertFalse(buffs.AstralFire(i) in u_list)
            self.assertTrue(buffs.UmbralIce(i) in u_list)
            self.assertFalse(buffs.UmbralIce(i) in a_list)
        self.assertTrue('Astral or Umbral' in a_list)
        self.assertTrue('Astral or Umbral' in u_list)


if __name__ == '__main__':
    unittest.main()
