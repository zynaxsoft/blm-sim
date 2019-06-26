""" Test buff related """
import unittest

from blmsim import buffs
from blmsim.util.time import Clock

class TestBuffs(unittest.TestCase):

    def test_buff_check_member_astral_umbral(self):
        a_list = [buffs.AstralFireBuff(1),
                  buffs.AstralFireBuff(2),
                  buffs.AstralFireBuff(3)]
        u_list = [buffs.UmbralIceBuff(1),
                  buffs.UmbralIceBuff(2),
                  buffs.UmbralIceBuff(3)]
        for i in range(1, 4):
            self.assertTrue(buffs.AstralFireBuff(i) in a_list)
            self.assertFalse(buffs.AstralFireBuff(i) in u_list)
            self.assertTrue(buffs.UmbralIceBuff(i) in u_list)
            self.assertFalse(buffs.UmbralIceBuff(i) in a_list)
        self.assertTrue('Astral or Umbral' in a_list)
        self.assertTrue('Astral or Umbral' in u_list)

    def test_buff_polyglot_no_expire_max_charge(self):
        polyglot = buffs.PolyglotBuff()
        polyglot.duration = Clock(0)
        self.assertFalse(polyglot.is_exhausted())
        self.assertEqual(polyglot.charge, 0)
        polyglot.gain_charge()
        self.assertEqual(polyglot.charge, 1)
        polyglot.gain_charge()
        self.assertEqual(polyglot.charge, 1)
        polyglot.renew(polyglot)
        self.assertEqual(polyglot.charge, 1)

    def test_buff_enochian_no_exipire(self):
        enochian = buffs.EnochianBuff()
        enochian.duration = Clock(0)
        self.assertFalse(enochian.is_exhausted())

if __name__ == '__main__':
    unittest.main()
