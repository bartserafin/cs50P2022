# re
# re.search(pattern, string, flags=0)

import re

email = input('What is your email? ')

if re.serach('@', email):
    print('Valid')
else:
    print('Invalid')


'''
. any character except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions
{m,n} m to n repetitions
'''

# r - raw string, to tell python not to look at it :D
# .+ 1 or more repetions of any character
# @
# .+ .+ 1 or more repetions of any character
# .enu

if re.serach(r'.+@.+\.edu', email):
    print('Valid')
else:
    print('Invalid')

# . any character once
# .* any character zero or more times
# @
# . any character once
# .* any character zero or more times
if re.serach('..*@..*', email):
    print('Valid')
else:
    print('Invalid')


'''
^ matches the start of the string
$ matches the end of the string just before
  the newline at the end of the string
'''

# ^ match start of the string
# .+ one more repetion of any character
# @
# .+ one more repetion of any character
# match the end of the string to .edu
if re.serach(r'^.+@.+\.edu$', email):
    print('Valid')
else:
    print('Invalid')

'''
[] set of characters
[^] any character but this character
'''

# ^ match the start of the string
# [^@]+ decline 1 or many repetions of @ before the single wanted @
# look for a single @
# [^@]+ decline 1 or many repetions of @ after the single wanted @
# \. - escape dot as an special sign, we literally want the end of the string to match
# .edu$
if re.serach(r'^[^@]+@[^@]\.edu$', email):
    print('Valid')
else:
    print('Invalid')

# restrictions to username and domain name
# [a-zA-Z0-9_] - onyl accept this range of letters and numbers and _
# [a-zA-Z0-9] this stands for aplhanumeric characters
if re.serach(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$', email):
    print('Valid')
else:
    print('Invalid')


# workarounds
# \w - any word character, alphanumercial or _
if re.serach(r'^\w+@\w+\.edu$', email):
    print('Valid')
else:
    print('Invalid')


'''
\d - allow decimal digit
\D - dont not a decimal digit
\s - allow whitespace characters
\S - dont not a whitespace characters
\w - allow word character
\W - dont not a word character
'''

# accpet more ending patterns
if re.serach(r'^\w+@\w+\.(edu|com|gov|net|org)$', email):
    print('Valid')
else:
    print('Invalid')

'''
A|B etiher is allowed
(...) a group is allowed
(?:...) non-capturing version
'''

# handling upper case for the extension e.g .EDU .COM
# using flags
'''
re.IGNORECASE
re.MULTILINE
re.DOTALL
'''
if re.serach(r'^\w+@\w+\.(edu|com|gov|net|org)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')


# handling dots after @
# serafin@cs50.hadvard.com
# (\w+\.)? - 0 or 1 repetion of (alphanumeric characters, and a single dot)
if re.serach(r'^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')


# handling dots before @
# bart.serafin@cs50.hadvard.com
if re.serach(r'^(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov|net|org)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')

