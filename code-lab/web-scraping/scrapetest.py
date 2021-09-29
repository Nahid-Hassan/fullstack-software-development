from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, "html.parser")

# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

nameList = bs.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text()) # .text and get_text() are not same

print(bs.find_all(text='the prince', limit=5))