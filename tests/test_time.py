""" _assertion of time """
import unittest
from blmsim.util.time import Clock, Time

class TestTime(unittest.TestCase):

    def test_time_comparing_equal(self):
        time_a = Time(30)
        time_b = Time(30)
        self.assertEqual(time_a, time_b)

    def test_time_comparing_not_equal(self):
        time_a = Time(30)
        time_b = Time(40)
        self.assertNotEqual(time_a, time_b)

    def test_time_comparing_greater_lesser(self):
        time_a = Time(30)
        time_b = Time(40)
        self.assertGreater(time_b, time_a)
        self.assertLess(time_a, time_b)

    def test_time_adding(self):
        time_a = Time(30)
        time_b = Time(40)
        tick_a = time_a.ticks
        tick_b = time_b.ticks
        self.assertEqual(time_a + time_b, Time(ticks=tick_a + tick_b))

    def test_time_subtracting(self):
        time_a = Time(30)
        time_b = Time(40)
        tick_a = time_a.ticks
        tick_b = time_b.ticks
        self.assertEqual(time_b - time_a, Time(ticks=tick_b - tick_a))

    def test_time_is_zero(self):
        time_a = Time(0)
        time_b = Time(1)
        self.assertTrue(time_a.is_zero())
        self.assertFalse(time_b.is_zero())

    def test_clock_hook(self):
        class TestHook:
            def __init__(self):
                self.tocked = 0
            def tock(self):
                self.tocked += 1
        clock = Clock(ticks=0)
        testhook = TestHook()
        clock.hook(testhook)
        clock.tick()
        self.assertEqual(testhook.tocked, 1)
        clock.unhook(testhook)
        clock.tick()
        self.assertEqual(testhook.tocked, 1)

    def test_clock_tick(self):
        clock = Clock(ticks=20)
        clock.tick()
        self.assertEqual(clock, Clock(ticks=21))

    def test_clock_negative_tock(self):
        clock = Clock(ticks=0)
        clock.tock()
        self.assertGreaterEqual(clock.ticks, 0)

    def test_clock_reset(self):
        clock = Clock(ticks=30)
        clock.reset()
        self.assertEqual(clock, Clock(ticks=0))
        clock = Clock(default=10)
        for _ in range(5):
            clock.tock()
        clock.reset()
        self.assertEqual(clock, Clock(10))

if __name__ == '__main__':
    unittest.main()
