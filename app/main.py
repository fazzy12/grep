#!/usr/bin/env python3
import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if pattern.startswith("^"):
        pattern = pattern[1:]  # Remove the "^" anchor from the pattern
        return input_line.startswith(pattern)
    elif pattern.endswith("$"):
        pattern = pattern[:-1]  # Remove the "$" anchor from the pattern
        return input_line.endswith(pattern)
    elif pattern.endswith("+"):
        pattern = pattern[:-1]  # Remove the "+" quantifier from the pattern
        if not pattern:
            raise RuntimeError("Invalid pattern: Quantifier without preceding character or class")
        return bool(re.search(f"{pattern}+", input_line))
    elif "+" in pattern:
        parts = pattern.split("+")
        if len(parts) != 2:
            raise RuntimeError("Invalid pattern: Multiple '+' quantifiers found")
        return bool(re.search(f"{parts[0]}+{parts[1]}", input_line))
    elif pattern.endswith("?"):
        pattern = pattern[:-1]  # Remove the "?" quantifier from the pattern
        return bool(re.search(f"{pattern}?", input_line))
    elif pattern == "\\d":
        return bool(re.search(r'\d', input_line))
    elif pattern == "\\w":
        return is_alphanumeric(input_line)
    elif len(pattern) == 1:
        return pattern in input_line
    else:
       False

def is_alphanumeric(input_str):
    return input_str.isalnum()

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    try:
        if match_pattern(input_line, pattern):
            print(f"Pattern '{pattern}' found: Exit status 0")
            exit(0)
        else:
            print("Pattern not found: Exit status 1")
            exit(1)
    except RuntimeError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
