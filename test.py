import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("трикутник", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

    def test_unknown_figure_type(self):
        with self.assertRaises(AssertionError):
            Figure("ромб", 3)

    def test_all_figure_types(self):
        for figure_type in Figure.FIGURES:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 4)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(4, figure.get_figure_length)

    def test_lengths_subtest(self):
        for length in [1, 5, 10]:
            with self.subTest(length=length):
                self.assertEqual(length, Figure("квадрат", length).get_figure_length)

    def test_angles_square(self):
        self.assertEqual([90, 90, 90, 90], Figure("квадрат", 5).get_angles())

    def test_angles_rectangle(self):
        self.assertEqual([90, 90, 90, 90], Figure("прямокутник", 5).get_angles())

    def test_angles_triangle(self):
        angles = Figure("трикутник", 5).get_angles()
        self.assertEqual([60, 60, 60], angles)
        self.assertEqual(180, sum(angles))


if __name__ == "__main__":
    unittest.main(verbosity=2)
