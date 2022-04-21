def main():
    user_text = input("What is your text? ")
    print(convert(user_text))


def convert(text):
    smiley_face = '🙂'
    sad_face = '🙁'
    converted_text = text.replace(":)", smiley_face)
    converted_text = converted_text.replace(":(", sad_face)
    return converted_text


main()