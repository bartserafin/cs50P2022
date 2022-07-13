from pyfiglet import Figlet
import sys
import random


def main():
    figlet_printer()



def figlet_printer():
    figlet = Figlet()

    # checks input
    if len(sys.argv) == 1:
        font = figlet.setFont(font=random.choice(figlet.getFonts()))

    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = sys.argv[2]
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
            else:
                figlet.setFont(font=font)
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv) > 3:
        sys.exit("Invalid usage")



    # prints text
    text = input()
    print(figlet.renderText(text))


main()


