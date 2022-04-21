print("#")
print("#")
print("#")
print("-------")

for _ in range(3):
    print("#")

print("-------")


def main():
    print_column(3)
    print_row(3)
    print_square(3)
    print_square_compact(3)


def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")
    print("-------")



def print_row(width):
    print("?" * width)
    print("-------")


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # after every row, go next line
        print()
    print("-------")


def print_square_compact(size):
    # for each row in square
    for i in range(size):
        # print size bricks
        print("#" * size)
    print("-------")


main()