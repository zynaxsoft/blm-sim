""" Test cases for targetdummy """
import unittest

from blmsim.targetdummy import TargetDummy, TargetObserver


class TestTargetDummy(unittest.TestCase):

    def test_dummy_damage_taken(self):
        dummy = TargetDummy()
        dummy.take_damage(20)
        dummy.take_potency(20)
        self.assertEqual(dummy.damage_taken, 20)
        self.assertEqual(dummy.potency_taken, 20)

    def test_observe_damage(self):
        dummy = TargetDummy()
        observer = TargetObserver()
        observer.eyes_on(dummy)
        for _ in range(10):
            dummy.take_damage(10)
            dummy.take_potency(10)
        self.assertEqual(observer.observe_total_damage_taken(), 100)
        self.assertEqual(observer.observe_total_potency_taken(), 100)


if __name__ == '__main__':
    unittest.main()
