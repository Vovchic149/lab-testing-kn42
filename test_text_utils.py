import unittest

from text_utils import count_symbols, count_vowels, divide


class TestCountSymbols(unittest.TestCase):
    def test_count_symbols(self):
        self.assertEqual(3, count_symbols("abc"))
        self.assertEqual(0, count_symbols(""))


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


class TestCountVowels(unittest.TestCase):
    def test_latin(self):
        self.assertEqual(2, count_vowels("hello"))

    def test_uppercase(self):
        self.assertEqual(3, count_vowels("AEI"))

    def test_no_vowels(self):
        self.assertEqual(0, count_vowels("rhythm"))

    def test_empty_string(self):
        self.assertEqual(0, count_vowels(""))

    def test_digits(self):
        self.assertEqual(0, count_vowels("12345"))

    def test_digits_with_vowels(self):
        self.assertEqual(1, count_vowels("a12345"))

    def test_ukrainian(self):
        self.assertEqual(4, count_vowels("Україна"))

    def test_ukrainian_special_letters(self):
        self.assertEqual(4, count_vowels("єїюя"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
