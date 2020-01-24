import urllib.request as url
import json

'''
path = "https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=35320"

res = url.urlopen(path)
data = json.load(res)
'''

path = "https://newsapi.org/v2/everything?q=apple&from=2020-01-23&to=2020-01-23&sortBy=popularity&apiKey=695e07af402f4b119f0703e9b19f4683"
res = url.urlopen(path)
data = json.load(res)

articles = data['articles']
for i in range(len(articles)):
    print("News --> ",i)
    print(articles[i]['title'])
    print("By -",articles[i]['author'])
    print("*"*20)
