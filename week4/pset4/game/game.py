import random
import sys

def main():
    game()


def game():

    guess = 0

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:

            while True:
                try:
                    # Set up
                    number = random.randint(1, level)

                    # Game Loop
                    guess = int(input("Guess: "))
                    if guess > number:
                        print("Too large!")
                    elif guess < number:
                        print("Too small!")
                    elif guess > level:
                        raise ValueError
                    else:
                        print("Just right!")
                        sys.exit()
                except ValueError:
                    continue


main()