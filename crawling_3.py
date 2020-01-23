import bs4
import urllib.request as url

for i in range(1,5):
    path = f"https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&as-pos=0&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=13868958-ffd5-4c66-b06b-5986e8db6d9c&as-backfill=on&page={i}"

    response = url.urlopen(path)

    page = bs4.BeautifulSoup(response,'lxml')

    div = page.findAll('div',class_='_3wU53n')
    price = page.findAll('div',class_='_1vC4OE _2rQ-NK')
    rating = page.findAll('div',class_='hGSR34')

    for j in range(len(div)):
        print(div[j].text)
        print("Price :",price[j].text)
        print("Rating :",rating[j].text)
        print("="*20)
