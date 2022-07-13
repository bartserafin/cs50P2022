import inflect

def main():
    adieu()


def adieu():
    p = inflect.engine()

    names = []

    while True:
        try:
            name = input()
            if not name in names:
                names.append(name)
        except EOFError:
            break

    names = p.join(names)
    print(f"Adieu, adieu, to {names}")


main()
