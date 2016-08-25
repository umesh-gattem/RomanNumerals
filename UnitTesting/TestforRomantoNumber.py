from romanNumbers import RomanToInteger
import unittest


class romanToInt(unittest.TestCase):
    test_cases = (
        ('XLV', 45),
        ('XC', 90),
        ('III', 3),
        ('DLXVII', 567),
        ('XLV', 45),
        ('D', 500),
    )

    def test_roman_to_int(self):
        for roman, number in self.test_cases:
            result = RomanToInteger.roman_to_integer(roman)
            self.assertEqual(result, number)


if __name__ == "__main__":
    unittest.main()
