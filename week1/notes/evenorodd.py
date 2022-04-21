def main():
    x = int(input())
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()


# Pythonic way
def is_even_v2(n):
    return True if n % 2 == 0 else False

def is_even_v3(n):
    return (n % 2 == 0) # this return True or False on its own :D
    