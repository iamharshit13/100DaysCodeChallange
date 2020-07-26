'''

import http.client

conn = http.client.HTTPSConnection("stock-google-news.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "stock-google-news.p.rapidapi.com",
    'x-rapidapi-key': "14ebc18036msh09f6d9fabd609b2p154a76jsn498b4f451979"
    }

conn.request("GET", "/v1/search?lang=en&country=US&ticker=AAPL", headers=headers)

res = conn.getresponse()
data = res.read()
for line in data.decode("utf-8"):
    print(line)
'''

import requests

url = "https://stock-google-news.p.rapidapi.com/v1/search"

querystring = {"lang":"en","country":"IND","ticker":"AAPL"}

headers = {
    'x-rapidapi-host': "#HOST",
    'x-rapidapi-key': "#KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
a = response.json()



for item in a['feed']:
#for item in response['feed']:
#    print(item['language'])
#print(type(response))
#print(response.text)
