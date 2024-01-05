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

    def test_question_mark_quantifier(self):
        self.assertTrue(match_pattern("dogs", "dogs?"))
        self.assertTrue(match_pattern("dog", "dogs?"))
        self.assertFalse(match_pattern("cat", "dogs?"))

    def test_wildcard_match(self):
        input_line = "dog"
            
        # Test pattern that should match
        pattern1 = "d.g"
        self.assertTrue(match_pattern(input_line, pattern1))

        # Test pattern that should not match
        pattern2 = "c.g"
        self.assertFalse(match_pattern(input_line, pattern2))
        
        
    def test_alternation_match(self):
        # Test if the pattern "(cat|dog)" matches "cat"
        self.assertTrue(match_pattern("cat", "(cat|dog)"))
            
        # Test if the pattern "(cat|dog)" matches "dog"
        self.assertTrue(match_pattern("dog", "(cat|dog)"))

        # Test if the pattern "(cat|dog)" does not match "apple"
        self.assertFalse(match_pattern("apple", "(cat|dog)"))

        # Test if the function raises a RuntimeError for an invalid pattern
        with self.assertRaises(RuntimeError):
            match_pattern("apple", "(cat|")
            


if __name__ == "__main__":
    unittest.main()
