import unittest
from leap_year import validated_is_leap_year

class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(validated_is_leap_year("2000"))

    def test_not_leap_year(self):
        self.assertFalse(validated_is_leap_year("2001"))

if __name__ == "__main__":
    unittest.main()
