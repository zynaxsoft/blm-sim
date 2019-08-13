import unittest
import tests

runner = unittest.TextTestRunner()
suite = unittest.TestLoader().discover('./tests')
runner.run(suite)
