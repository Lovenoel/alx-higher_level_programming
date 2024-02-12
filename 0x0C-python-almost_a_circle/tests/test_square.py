#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_instance_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(2)
        self.assertEqual(s.display(), None)  # It's hard to test the display output, so we just check if it doesn't error

    def test_str(self):
        s = Square(5, 1, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 9, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 9})

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, x=2, y=3, id=4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, size=1, x=2, y=3, id=4)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")


if __name__ == "__main__":
    unittest.main()

