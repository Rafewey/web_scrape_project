from urllib.request import urlopen
from bs4 import BeautifulSoup

#Creating a txt file to write on
#f = open("scrapped_info.txt", "w+")
f = open("scrapped_info.txt", "w+")

#Grabbing the page
url = "http://quotes.toscrape.com/"
response = urlopen(url)
page_html = response.read()

#Parsing
page_soup = BeautifulSoup(page_html, "html.parser")
quotes = page_soup.findAll("div",{"class":"quote"})

for quote in quotes:
    f.write("{quote} --- {author} \n".format(quote=quote.span.text, author=quote.small.text))

response.close()
f.close()