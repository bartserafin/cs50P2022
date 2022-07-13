# Demonstrates requests

import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
)
ugly_print = response.json()
pretty_print = json.dumps(ugly_print, indent=2)
print(pretty_print)

all_songs = response.json()
for result in all_songs["results"]:
    print(result["trackName"])