def main():
    current_time = input("What is the time? ")
    convert(current_time)


def convert(time):
    time = time.split(":")
    hours = int(time[0])
    minutes = int(time[-1])
    total_time = hours + minutes / 60
    pick_a_meal(total_time)


def pick_a_meal(time):
    """
    eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
    """
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time < 19:
        print("Dinner time")


if __name__ == "__main__":
    main()