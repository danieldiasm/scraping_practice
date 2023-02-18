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
scrape_list = ["Name", "Favorite Color"]
extracted_text = {}

for scrape in scrape_list:
    start_addr = page_text.find(scrape)
    start_txt_addr = start_addr + len(scrape)

    next_tag_offset = page_text[start_txt_addr:].find('<')
    end_text_addr = next_tag_offset + start_txt_addr

    raw = page_text[start_txt_addr : end_text_addr]
    clean = raw.strip(': \r\t\n')

    extracted_text[scrape] = clean

# Print the result
print(extracted_text)
