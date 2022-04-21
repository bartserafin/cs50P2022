# while

i = 0
while i != 3:
    print("-- meow --")
    i += 1

# for
for i in [0, 1, 2]:
    print('meow')

for i in range(10):
    print(f" {i} - 'meow'")

# if we dont use 'i' we can skip it with "_"
for _ in range(10):
    print("Meow!")

# pythonic way
print("meow\n" * 3, end="")


# break
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("How many meow's? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()