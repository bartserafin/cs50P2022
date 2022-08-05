import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    # collect src, only embed/....
    if matches := re.search(r'.+src=".+?embed/(.+?)".+', s):
        embed = matches.group(1)

        # return a shorter youtu.be/... version
        return 'https://youtu.be/' + embed
    else:
        return





if __name__ == "__main__":
    main()