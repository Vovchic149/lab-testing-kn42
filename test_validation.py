import unittest

from validation import check_positive_number


class TestCheckPositiveNumber(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(5.0, check_positive_number("5"))

    def test_valid_float(self):
        self.assertEqual(3.5, check_positive_number("3.5"))

    def test_negative(self):
        with self.assertRaises(ValueError):
            check_positive_number("-3")

    def test_zero(self):
        with self.assertRaises(ValueError):
            check_positive_number("0")

    def test_not_a_number(self):
        with self.assertRaises(ValueError):
            check_positive_number("abc")

    def test_empty(self):
        with self.assertRaises(ValueError):
            check_positive_number("")


if __name__ == "__main__":
    unittest.main(verbosity=2)
