import unittest
from fibonacci import fib

class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(fib(1), 1)

    def testCase2(self):
        self.assertEqual(fib(5), 5)

    def testCase3(self):
        self.assertEqual(fib(12), 144)

if __name__ == "__main__":
    unittest.main()