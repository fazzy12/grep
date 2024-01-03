#!/usr/bin/python3
import unittest
from app.main import match_pattern

class TestMatchPattern(unittest.TestCase):

    def test_startswith_anchor(self):
        self.assertTrue(match_pattern("apple", "^app"))

    def test_endswith_anchor(self):
        self.assertTrue(match_pattern("apple", "ple$"))

    def test_plus_quantifier_at_end(self):
        self.assertTrue(match_pattern("caaats", "ca+ts"))

    def test_plus_quantifier_in_middle(self):
        self.assertTrue(match_pattern("caaats", "ca+ts"))

    def test_invalid_plus_quantifier(self):
        with self.assertRaises(RuntimeError):
            match_pattern("apple", "a++ple")

    def test_digit_class(self):
        self.assertTrue(match_pattern("apple1", "\\d"))

    def test_word_class(self):
        self.assertTrue(match_pattern("apple", "\\w"))

    def test_single_character(self):
        self.assertTrue(match_pattern("apple", "a"))

    def test_pattern_not_found(self):
        self.assertFalse(match_pattern("orange", "app"))
        
    # Test for pattern with start anchor and end anchor
    def test_start_and_end_anchors(self):
        self.assertTrue(match_pattern("apple", "^app.*le$"))

    # Test for pattern with multiple characters followed by '+' quantifier
    def test_multiple_characters_plus_quantifier(self):
        self.assertTrue(match_pattern("caaats", "ca+ts"))

    # Test for pattern with special characters
    def test_pattern_with_special_characters(self):
        self.assertTrue(match_pattern("apple#123", "\\w+#\\d+"))

    # Test for pattern with escaped characters
    def test_escaped_character(self):
        self.assertTrue(match_pattern("apple\\", "apple\\$"))

    # Test for pattern with multiple '+' quantifiers
    def test_invalid_multiple_plus_quantifiers(self):
        with self.assertRaises(RuntimeError):
            match_pattern("caaats", "ca+ts+")

    # Test for pattern not found with start anchor
    def test_pattern_not_found_with_start_anchor(self):
        self.assertFalse(match_pattern("orange", "^app"))

    # Test for pattern not found with end anchor
    def test_pattern_not_found_with_end_anchor(self):
        self.assertFalse(match_pattern("apple", "le$"))

    # Test for pattern not found with digit class
    def test_pattern_not_found_with_digit_class(self):
        self.assertFalse(match_pattern("apple", "\\d"))

    # Test for pattern not found with word class
    def test_pattern_not_found_with_word_class(self):
        self.assertFalse(match_pattern("apple", "\\w"))

    # Test for pattern not found with single character
    def test_pattern_not_found_with_single_character(self):
        self.assertFalse(match_pattern("apple", "z"))

    # Test for pattern not found with special characters
    def test_pattern_not_found_with_special_characters(self):
        self.assertFalse(match_pattern("apple", "\\$"))

    # Test for pattern not found with escaped characters
    def test_pattern_not_found_with_escaped_characters(self):
        self.assertFalse(match_pattern("apple", "\\"))

    # Test for pattern not found with invalid pattern
    def test_pattern_not_found_with_invalid_pattern(self):
        with self.assertRaises(RuntimeError):
            match_pattern("apple", "a**ple")

    # Test for pattern not found with empty input line
    def test_pattern_not_found_with_empty_input_line(self):
        self.assertFalse(match_pattern("", "\\w"))

    # Test for pattern not found with empty pattern
    def test_pattern_not_found_with_empty_pattern(self):
        self.assertFalse(match_pattern("apple", ""))

    # Test for pattern not found with None input line
    def test_pattern_not_found_with_none_input_line(self):
        self.assertFalse(match_pattern(None, "\\w"))

    # Test for pattern not found with None pattern
    def test_pattern_not_found_with_none_pattern(self):
        self.assertFalse(match_pattern("apple", None))


if __name__ == "__main__":
    unittest.main()
