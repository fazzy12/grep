#!/usr/bin/env python3
import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if pattern.startswith("^"):
        pattern = pattern[1:]
        return input_line.startswith(pattern)
    elif pattern.endswith("$"):
        pattern = pattern[:-1]
        return input_line.endswith(pattern)
    elif pattern == "\\d":
        return bool(re.search(r'\d', input_line))
    elif pattern == "\\w":
        return is_alphanumeric(input_line)
    elif len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def is_alphanumeric(input_str):
    return input_str.isalnum()

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        print(f"Pattern '{pattern}' found: Exit status 0")
        exit(0)
    else:
        print("Pattern not found: Exit status 1")
        exit(1)

if __name__ == "__main__":
    main()
