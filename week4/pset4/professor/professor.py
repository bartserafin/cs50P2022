import random


def main():
    DIFFICULTY = 10
    score = 0
    number_digits = get_level()
    game_loop(DIFFICULTY, number_digits)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level >= 4:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def game_loop(number_of_problems, digits):
    score = 0

    for _ in range(number_of_problems):
        tries = 3
        x, y = generate_integer(digits), generate_integer(digits)
        guess = None
        answer = x + y

        while guess != answer:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess != answer:
                    raise ValueError
                else:
                    score += 1
                    break
            except ValueError:
                tries -= 1
                print("EEE")
                if tries == 0:
                    print(f"{x} + {y} = {answer}")
                    break
                else:
                    continue

    print(f"Score: {score}")




if __name__ == "__main__":
    main()