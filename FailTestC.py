import unittest

from demo import PrimeChecker


class TestPrimeChecker(unittest.TestCase):
    
    def test_fail_simple(self):
        a = 4
        res = PrimeChecker(a)
        self.assertEqual(res,True)

    def test_fail_medium(self):
        a = 27
        res = PrimeChecker(a)
        self.assertEqual(res,True)


if __name__ == "__main__":
    unittest.main()