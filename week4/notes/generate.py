# this imports everything from random module
# import random

# coin = random.choice(["heads", "tails"])
# print(coin)


# use this to import the specific functions
from random import choice, randint, shuffle

coin = choice(["heads", "tails"])
print(coin)

# randint(a, b) from a and b inclusive
number = randint(1, 10)
print(number)

# shuffle(list) - shuffles the list, like a deck of cards
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)