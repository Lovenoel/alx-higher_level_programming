#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_instance_creation(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_display(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)  # It's hard to test the display output, so we just check if it doesn't error

    def test_str(self):
        r = Rectangle(5, 5, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 5/5")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (10) 3/4 - 2/1")

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, height=1, width=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/1")


if __name__ == "__main__":
    unittest.main()
