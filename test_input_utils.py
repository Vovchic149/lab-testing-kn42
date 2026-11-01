import unittest
from unittest.mock import patch

from input_utils import ask_number


class TestAskNumber(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_valid_input(self, mock_input):
        self.assertEqual(5.0, ask_number())
        mock_input.assert_called_once_with("Введіть число: ")

    @patch("builtins.input", return_value="-1")
    def test_negative_input(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="abc")
    def test_text_input(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
