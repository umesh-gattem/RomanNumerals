from romanNumbers import IntegertoRoman
import unittest


class intToRoman(unittest.TestCase):
    test_cases = (
        ('XLV', 45),
        ('XC', 90),
        ('III', 3),
        ('DLXVII', 567),
        ('XLV', 45),
        ('XLIII',42)
    )

    def test_int_to_roman(self):
        for roman, number in self.test_cases:
            result = IntegertoRoman.integer_to_roman(number)
            self.assertEqual(roman, result)


if __name__ == "__main__":
    unittest.main()
