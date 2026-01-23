#!/usr/bin/python3
"""Unittest for max_integer function."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_at_beginning(self):
        """Test when max is at the beginning."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_in_middle(self):
        """Test when max is in the middle."""
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)


if __name__ == '__main__':
    unittest.main()
