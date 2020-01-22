Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> import urllib.request as url
>>> path = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on"
>>> res = url.urlopen(path)
>>> page = bs4.BeautifulSoup(res,'lxml')
>>> len(page)
3
>>> type(page)
<class 'bs4.BeautifulSoup'>
>>> page.find('div',class_='_3wU53n')
<div class="_3wU53n">Samsung Super 6 138cm (55 inch) Ultra HD (4K) LED Smart TV</div>
>>> div = page.find('div',class_='_3wU53n')
>>> print(div)
<div class="_3wU53n">Samsung Super 6 138cm (55 inch) Ultra HD (4K) LED Smart TV</div>
>>> div.text
'Samsung Super 6 138cm (55 inch) Ultra HD (4K) LED Smart TV'
>>> 
