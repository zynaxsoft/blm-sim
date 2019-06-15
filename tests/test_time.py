import unittest
from blmsim.util.time import Clock, Time

class TestTime(unittest.TestCase):

    def test_time_comparing_equal(self):
        timeA = Time(30)
        timeB = Time(30)
        self.assertEqual(timeA, timeB)

    def test_time_comparing_not_equal(self):
        timeA = Time(30)
        timeB = Time(40)
        self.assertNotEqual(timeA, timeB)

    def test_time_comparing_greater_lesser(self):
        timeA = Time(30)
        timeB = Time(40)
        self.assertGreater(timeB, timeA)
        self.assertLess(timeA, timeB)

    def test_time_adding(self):
        timeA = Time(30)
        timeB = Time(40)
        tickA = timeA.ticks
        tickB = timeB.ticks
        self.assertEqual(timeA + timeB, Time(ticks=tickA + tickB))

    def test_time_subtracting(self):
        timeA = Time(30)
        timeB = Time(40)
        tickA = timeA.ticks
        tickB = timeB.ticks
        self.assertEqual(timeB - timeA, Time(ticks=tickB - tickA))

    def test_time_is_zero(self):
        timeA = Time(0)
        timeB = Time(1)
        self.assertTrue(timeA.is_zero())
        self.assertFalse(timeB.is_zero())

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
        for i in range(5):
            clock.tock()
        clock.reset()
        self.assertEqual(clock, Clock(10))

if __name__ == '__main__':
    unittest.main()
