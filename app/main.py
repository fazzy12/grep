#!/usr/bin/env python3
import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!

def match_pattern(input_line, pattern):
    pattern_index = 0
    
    for char in input_line:
        if pattern_index >= len(pattern):
            return False
            
        if pattern[pattern_index] == "\\d":
            if not char.isdigit():
                return False
        elif pattern[pattern_index] == "\\w":
            if not char.isalnum():
                return False
        elif pattern[pattern_index] != char:
            return False
        
        pattern_index += 1
    
    return pattern_index == len(pattern)

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
