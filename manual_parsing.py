from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
print(f"From page {url}")
page = urlopen(url)
print("Retrieving from the URL, a object is returned:")
print(page)

html = page.read().decode("utf-8")
print("Decode to UTF-8 using decode:")
print(html)

pattern = "<title.*?>.*?</title.*?>"

match_results = re.search(pattern, html, re.IGNORECASE)  # This will return a MatchObject
title = match_results.group()  # MatchObject return the first, inclusive result.

title = re.sub("<.*?>", "", title)  # Remove HTML tags, replacing with nothing

# Show the result
print(title)
