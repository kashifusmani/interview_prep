import unittest

from test import test_me

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(test_me(), "test")  # add assertion here


if __name__ == '__main__':
    unittest.main()
