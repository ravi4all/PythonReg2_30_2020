import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on"

response = url.urlopen(path)

page = bs4.BeautifulSoup(response,'lxml')

div = page.findAll('div',class_='_3wU53n')
price = page.findAll('div',class_='_1vC4OE _2rQ-NK')
rating = page.findAll('div',class_='hGSR34')

for i in range(len(div)):
    print(div[i].text)
    print("Price :",price[i].text)
    print("Rating :",rating[i].text)
    print("="*20)
