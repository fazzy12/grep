# grep-like Utility in Python

This project aims to provide a simplified `grep`-like utility using Python. It allows users to search for patterns within input text, supporting a range of regular expression features.

## Features

- **Basic Pattern Matching**: Supports simple character-based pattern matching.
- **Anchors**: Recognizes patterns starting or ending with specific characters.
- **Quantifiers**: Supports patterns with quantifiers like `+` and `?`.
- **Wildcards**: Recognizes the `.` character as a wildcard for any single character.
- **Alternation**: Handles patterns with the `|` operator to match either of two patterns.

## Usage

To run the program:

```
$ echo "input_text" | ./app/main.py -E "pattern"
```

* **input_text**: The text you want to search within.
* **pattern**: The regular expression pattern you want to match against.

The program will exit with status `0` if a match is found and `1` otherwise.

## Dependencies

* Python 3.x
* No external libraries required.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new `Pull Request`.
