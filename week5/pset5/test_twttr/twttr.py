def main():
    user_text = input()
    print(shorten(user_text))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U"]
    shortend = ""
    for letter in word:
        if letter not in vowels and letter not in vowels.lower():
            shortend += letter
    return shortend


if __name__ == "__main__":
    main()