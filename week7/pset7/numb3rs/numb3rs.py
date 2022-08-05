import re
import sys

# valid ip address - #.#.#.# where # is a int between 0 and 255 inclusive
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    matches = re.search(r'(\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}', ip)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()