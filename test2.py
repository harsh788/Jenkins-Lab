import unittest
from fibonacci import fib


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(fib(-2), 1)

    def testCase2(self):
        self.assertEqual(fib(6.9), 2)


if __name__ == '__main__':
    unittest.main()