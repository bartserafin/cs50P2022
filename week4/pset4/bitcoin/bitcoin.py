import sys
import requests


def main():
    x = get_float()
    get_bitcoin_price(x)


def get_float():
    while True:
        try:
            number = float(sys.argv[1])
            return number
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except IndexError:
            sys.exit("Missing command line agument")


def get_bitcoin_price(number_of_bitcoins):
    try:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(data.json())
        index_price = float(data.json()['bpi']['USD']['rate_float'])
        price = index_price * number_of_bitcoins
        print(f"${price:,.4f}")
    except NameError:
        sys.exit("Invalid JSON read")


main()