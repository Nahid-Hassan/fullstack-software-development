# Web Scraping with Python

- [Web Scraping with Python](#web-scraping-with-python)
  - [Your First Web Scraper](#your-first-web-scraper)
    - [HTTPError and URLError](#httperror-and-urlerror)
    - [An Useful Example (Get title of the page)](#an-useful-example-get-title-of-the-page)

## Your First Web Scraper

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

soup = BeautifulSoup(html, "html.parser") # other html parser is "lxml", "html5lib"
print(soup)
```

### HTTPError and URLError

```py
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It worked!")
    # bsObj = BeautifulSoup(html.read(), "html.parser")
    # print(bsObj.h1)
```


### An Useful Example (Get title of the page)

```py
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title('http://www.pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')
else:
    print(title)
```

## Advanced HTML Parser

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, "html.parser")

# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

nameList = bs.find_all("span", {"class": "green"})
for name in nameList:
    print(name.get_text()) # .text and get_text() are not same

print(bs.find_all(text='the prince', limit=5))
```