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

    elif pattern.endswith("+"):
        pattern = pattern[:-1]
        if not pattern:
            raise RuntimeError("Invalid pattern: Quantifier without preceding character or class")
        return bool(re.search(f"{pattern}+", input_line))

    elif "+" in pattern:
        parts = pattern.split("+")
        if len(parts) != 2:
            raise RuntimeError("Invalid pattern: Multiple '+' quantifiers found")
        return bool(re.search(f"{parts[0]}+{parts[1]}", input_line))

    elif pattern.endswith("?"):
        pattern = pattern[:-1]
        return bool(re.search(f"{pattern}?", input_line))

    elif "." in pattern:
        escaped_pattern = re.escape(pattern)
        regex_pattern = escaped_pattern.replace("\\.", ".")
        return bool(re.search(regex_pattern, input_line))

    elif "|" in pattern:
        processed_patterns = []
        sub_patterns = pattern.split('|')
        for sub_pattern in sub_patterns:
            if sub_pattern[0] == "(" and sub_pattern[-1] == ")":
                sub_pattern = sub_pattern[1:-1]
                processed_patterns.append(sub_pattern)

        # Check if the input line matches any of the processed subpatterns
        for processed_pattern in processed_patterns:
            if re.search(processed_pattern, input_line):
                return True
        return False

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


# def extract_subpatterns(pattern):
#     subpatterns = []
#     depth = 0
#     start = 0

#     for i, char in enumerate(pattern):
#         if char == '(':
#             depth += 1
#             if depth == 1:
#                 start = i + 1
#         elif char == ')':
#             depth -= 1
#             if depth == 0:
#                 subpatterns.append(pattern[start:i])
#                 start = i + 1
#         print(f"Depth: {depth}")  # For debugging
#     return subpatterns

# def process_subpattern(sub):
#     # Remove leading and trailing parentheses
#     if sub.startswith('(') and sub.endswith(')'):
#         sub = sub[1:-1]
#     print(f"Subpattern: {sub}")  # For debugging
#     return sub.strip()

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
