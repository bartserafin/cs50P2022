# ask for twitter url
# extract user name from url

import re
# re.sub(pattern, repl, string, count=0, flags=0)
url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f' Username: {username}')

print('---------')
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", {matches.group(3)}) # <-- 3


# use non-capturing version of grouping, so we only capture one group
domain_lst = ['com', 'edu', 'org']
print('---------')
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.(.+)/([\w])+", url, re.IGNORECASE):
    if matches.group(1) in domain_lst: # <-- 1
        print(f"Username:", {matches.group(2)}) # <-- 2