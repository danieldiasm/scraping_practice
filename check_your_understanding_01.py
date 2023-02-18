# First exercise of "Check Your Understanding"
from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

# request the page and store the returned object
page_obj = urlopen(url)

# Read the buffer and throw into a str
page_bin = page_obj.read()

# Translate it from bytes to UTF-8
page_text = page_bin.decode('utf-8')

# Regex over the text to find whatever we want
# "Name:" and "Favorite Color:"
result = dict()
result['name_start'] = page_text.find("<h2>") + 4
result['name_end'] = page_text.find("</h2>")
result['name_content'] = page_text[result['name_start']:result['name_end']]

# Print the result
print(result)
