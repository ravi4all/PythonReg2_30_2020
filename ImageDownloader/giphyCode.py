import urllib.request as url
import json

finalInput = input("Enter your query : ")
finalInput = finalInput.replace(" ","+")
path = f'http://api.giphy.com/v1/gifs/search?q={finalInput}&api_key=bc56161131654faeb550630b83e0c977&limit=10'

res = url.urlopen(path)
data = json.load(res)

data = data['data']
for i in range(len(data)):
    img = data[i]['images']
    img_url = img['original']['url']

    url.urlretrieve(img_url, f'img_{i}.gif')
