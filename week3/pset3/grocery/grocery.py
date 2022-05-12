def main():
    grocery_dict()


def grocery_dict():
    dict = {}

    while True:
        try:
            item = input().upper()
            if item not in dict.keys():
                dict.update({item : 1})
            else:
                dict[item] += 1
        except EOFError:
            break

    for key in sorted(dict):
        print(dict[key], key)


main()