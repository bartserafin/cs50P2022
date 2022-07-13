import emoji

def main():
    emote_this()


def emote_this():
    emote_name = input("Input: ")
    print("Output:", emoji.emojize(emote_name))


main()
