import requests

url = "https://inspirobot.me/api?generateFlow=1"
def getData():
    r = requests.get(url)
    return r.json()

def getQuote():
    data = getData()
    return data['data'][1]['text']

