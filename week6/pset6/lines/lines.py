import sys

def main():
    validate()
    count_lines()

def validate():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return True

def count_lines():
    counter = 0
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            if line.strip().startswith("#"):
                continue
            if not line.strip():
                continue
            else:
                counter +=1
    return print(counter)



if __name__ == "__main__":
    main()