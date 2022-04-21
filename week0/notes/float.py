
# 1.2 , 3.4
x = float(input("What's x? "))
y = float(input("What's y? "))
result = x + y
print(result)

# round up to the nearest int
# round(number[, ndigits]) - optionally enter the number of decimals
print(f"Round up {x} + {y} is {round(result, 2)}")

# format to 1,000 fo US system writing
print(f"{result:,}")

x = float(input("What's x? "))
y = float(input("What's y? "))

# another round function using f-string
z = x / y
print(f"{z:.2f}")