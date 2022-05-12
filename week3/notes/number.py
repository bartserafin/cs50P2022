try:
    x = int(input("What is x? "))

except ValueError: #  incorrect data type usually
    print("x is not an integer")

except NameError: #  a variable is not defined
    print("x is invalid.")

else: #  you land here is no Errors where raised
    print(f"x is {x}")

finally:
    print("This is always printed no matter what.")