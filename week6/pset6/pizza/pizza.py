import sys
import csv
from tabulate import tabulate

def main():
    validate()
    pretty_print()

def validate():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        return True

def pretty_print():
    menu = []
    with open(sys.argv[1]) as file:
        for line in csv.reader(file, delimiter=","):
            menu.append(line)


    return print(tabulate(menu, headers='firstrow', tablefmt="grid"))



if __name__ == "__main__":
    main()
