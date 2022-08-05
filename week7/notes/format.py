# reformat username
import re
name = input("What is your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f'{first} {last}'
print(f'hello, {name}')



matches = re.search(r"^(.+), (.+)$", name)
if matches:
    # last = matches.group(1)
    # first = matches.group(2)
    name = matches.group(2) + " " + matches.group(1)
print(name)


# tidy up
# this is kindda new
# assign matches to re.serach and also ask a boolean
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(name)
