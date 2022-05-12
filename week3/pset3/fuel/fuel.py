def main():
    fuel_gauge = get_fuel("Fraction: ")
    print(fuel_gauge)


def get_fuel(prompt):
    while True:
        fraction = input(prompt).split("/")

        try:
            result = int(fraction[0]) / int(fraction[1]) * 100
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    if result > 100:
        get_fuel(prompt)
    if result >= 99:
        return "F"
    elif result <=1:
        return "E"
    else:
        return "{:.0f}".format(result) + "%"


main()