import string as st

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def two_letters(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def six_two(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def numbers_at_end(s):
    number_found = False

    for char in s:
        if char.isalpha() and number_found == True:
            return False
        elif char.isnumeric():
            number_found = True
    else:
        return True

def first_number_not_zero(s):
    for char in s:
        if char.isalpha():
            continue
        if char.isnumeric() and char == "0":
            return False
        else:
            return True
    return True

def no_marks(s):
    for char in s:
        if char in st.punctuation:
            return False
    return True


def is_valid(s):
    if two_letters(s):
        if six_two(s):
            if numbers_at_end(s):
                if first_number_not_zero(s):
                    if no_marks(s):
                        return True
    else:
        return False


main()