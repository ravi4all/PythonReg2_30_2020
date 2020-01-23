import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on"

#1. hit the url from where you want to fetch (crawl) the data
response = url.urlopen(path)

#2. send the response to beautiful soup class
page = bs4.BeautifulSoup(response,'lxml')

#3. now from page we can find the tag which contains the date we want
div = page.find('div',class_='_3wU53n')
price = page.find('div',class_='_1vC4OE _2rQ-NK')
rating = page.find('div',class_='hGSR34')

#4. after getting the tag now we want the text part from the tag
print(div.text)
print(price.text)
print(rating.text)
