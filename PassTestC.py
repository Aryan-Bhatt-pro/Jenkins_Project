import unittest

from demo import PrimeChecker


class TestPrimeChecker(unittest.TestCase):
    def test_simple(self):
        a = 2
        res = PrimeChecker(a)
        self.assertEqual(res, True)

    def test_medium(self):
        a = 67
        res = PrimeChecker(a)
        self.assertEqual(res, True)

    def test_hard(self):
        a = 1009
        res = PrimeChecker(a)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
