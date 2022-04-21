def hello(name):
    print(f"Hello, {name}")

hello(input("What is your name? "))


# scope
# all variables defined outside the function cannot be accsessed outside of the funtion
def vars(a, b, c):
    a = 10
    b = 12
    c = 13
    print(f"Vars are: {a, b, c}")

# print(a, b, c) - will generate NameError, since a, b, c are accessable only inside the funtion

# return
# use return if we want to use the result of a function, otherwise, function return None
def main():
    x = int(input("what is x? "))
    print("x squares is", square(x))

def square(n):
    return n ** 2

main()

def return_none():
    print("Nothing here.")
    return

print(return_none())