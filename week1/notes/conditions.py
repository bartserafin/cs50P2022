x = int(input("x ") )
y = int(input("y "))

# every if is asked from top to bottom
# regardless, if it gives True or False
if x < y:
    print(f"x - {x} is less than y - {y}.")
if x > y:
    print(f"x - {x} is more than y - {y}.")
if x == y:
    print(f"x - {x} is to y - {y}.")


# alternatively
# only one if will be anserwered
# if first "if" return True, elif wont be considered
if x < y:
    print(f"x - {x} is less than y - {y}.")
elif x > y:
    print(f"x - {x} is more than y - {y}.")
else x == y:
    print(f"x - {x} is to y - {y}.")


# "or"
if x < y or x > y:
    print("x is not eqaul to y")
else:
    print("x is eqaul to y")

# "and"
if x < y and x > y: # this is impossible
    print("Not possible.")

# !=
if x != y:
    print("x is not eqaul to y")