import re


def main():
    print(count(input("Text: ")))


def count(s):
    """Count the number of 'um' words in input and return it as an int"""
    matches = re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()