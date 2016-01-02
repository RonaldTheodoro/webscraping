from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://pythonscraping.com/exercises/exercise1.html')
bsObj = BeautifulSoup(html.read())

print(bsObj.h1)
