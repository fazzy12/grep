#!/usr/bin/env python3
import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if pattern.startswith("[") and pattern.endswith("]"):  # Check for positive character group
        characters = pattern[1:-1]  # Extract characters within square brackets
        return any(char in input_line for char in characters)
    elif pattern == "\\d":  # Check for the \d character class
        return bool(re.search(r'\d', input_line))
    elif pattern == "\\w":  # Check for the \w character class
        return is_alphanumeric(input_line)
    elif len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def is_alphanumeric(input_str):
    return input_str.isalnum()


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    matched_pattern = match_pattern(input_line, pattern)
    if matched_pattern:
        print(f"Pattern '{matched_pattern}' found: Exit status 0")
    else:
        print("Pattern not found: Exit status 1")

if __name__ == "__main__":
    main()
