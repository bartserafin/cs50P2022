def main():
    get_order()


def get_order():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total_price = 0

    while True:
        try:
            item = input("Item: ").title()

            for key in menu.keys():
                if item == key:
                    total_price += menu[key]
            print("Total: $" + "{:.2f}".format(total_price))
            
        except EOFError:
            print("\n")
            break
        except KeyError:
            pass


main()
