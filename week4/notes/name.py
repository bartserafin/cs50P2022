import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     print("Too few argumnets.")
# elif len(sys.argv) > 2:
#     print("Too many arguments.")
# else:
#     print("Hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few argumnets.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")
else:
    print("Hello, my name is", sys.argv[1])
