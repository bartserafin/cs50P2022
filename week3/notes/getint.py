def main():
    x = get_int("What is x? ")
    print(f"x is {x}.")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
            #print("x is not an integer.")


main()