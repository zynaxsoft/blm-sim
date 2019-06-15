import unittest
from blmsim.util.time import Clock, Time

class TestTime(unittest.TestCase):

    def test_comparing_equal_time(self):
        timeA = Time(30)
        timeB = Time(30)
        self.assertEqual(timeA, timeB)

    def test_comparing_not_equal_time(self):
        timeA = Time(30)
        timeB = Time(40)
        self.assertNotEqual(timeA, timeB)

if __name__ == '__main__':
    unittest.main()
