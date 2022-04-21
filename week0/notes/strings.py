print('hello, world')

name = input("What's your name? ")
print('hello, '+ name)

# this is a print default
# print(*args, end=" ", sep=" ")

# lets overwirte the end= " " so two print functions actually print on the same line
print('Hello, ', end="")
print(name)

# escaping characters
print("Hello, \"Friend\"")

# f-string formating
print(f"Hello, {name}!!.")

# remove whitespace from a string
# .strip() removes whitespaces by deafult
white_space = "Hello, General Kenobi    "
white_sapce = white_space.strip()
print(white_space)

# remove another white characters
white_a = 'Helloyaaaaa'
white_a = white_a.strip('a')
print(white_a)

# Capitalize string
# capitalize only the first letter
cap = "title"
cap = cap.capitalize()

# Title string
# Capitazlie all first letters
book_title = 'alice in the wonderlands'
book_title = book_title.title()
print(book_title)

# we can chain methods
strip_cap_me = 'bartosz serafin   '
strip_cap_me = strip_cap_me.strip().title()
print(strip_cap_me)