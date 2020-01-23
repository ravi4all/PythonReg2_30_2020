import bs4
import urllib.request as url

movie_name = input("Enter movie name : ")
movie_name = movie_name.replace(' ','+')
path = "https://www.imdb.com/find?q="+movie_name

res = url.urlopen(path)
page = bs4.BeautifulSoup(res,'lxml')
td = page.find('td',class_='result_text')
a_tag = td.find('a')

newPath = "https://www.imdb.com"+a_tag['href']
res = url.urlopen(newPath)
page_2 = bs4.BeautifulSoup(res,'lxml')

title = page_2.find('div',class_='title_wrapper')
title = title.text.split()
print(' '.join(title))
