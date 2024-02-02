#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_order(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 5, 0]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.2]), 4.2)

    def test_string_values(self):
        with self.assertRaises(TypeError):
            max_integer(["one", "two", "three"])

if __name__ == '__main__':
    unittest.main()
