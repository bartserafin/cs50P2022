def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # $33.33
    d = float(d.replace("$", "")) / 100
    return d


def percent_to_float(p):
    # 32%
    p = float(p.replace("%", ""))
    return p


main()