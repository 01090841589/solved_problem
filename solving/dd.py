import requests
url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
print(data)