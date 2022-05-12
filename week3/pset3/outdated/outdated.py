def main():
    get_date()


def check_date(year, month, day):
    if year < 1:
        return False
    elif month > 12:
        return False
    elif day > 31:
        return False
    else:
        return True


def get_date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            date = input("Date: ")

            if "/" in date:
                date = date.split("/")
                year = int(date[2])
                month = int(date[0])
                day = int(date[1])

                if check_date(year, month, day):
                    print(f"{year}" + "-" + f"{month:02}" + "-" + f"{day:02}")
                    break

            elif "," in date:
                date = date.split(" ")

                month = date[0]
                if month not in months:
                    raise IndexError
                else:
                    for month in months:
                        if month == date[0]:
                            month_index = months.index(month) + 1 # +1 because January is the first month and have index of 0

                year = int(date[2])
                month = month_index
                day = int(date[1][:-1])

                if check_date(year, month, day):
                    print(f"{year}" + "-" + f"{month_index:02}" + "-" + f"{day:02}")
                    break

        except IndexError:
            pass
        except ValueError:
            pass


main()