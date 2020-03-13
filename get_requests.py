import requests
import urllib.parse
import json

# URL = path =arguments
# Headers and metadata
# GET REQUESTS
# Postcodes.io  ---> Follow Documentation
# Capture the input ----> decrypt Jason into dictionary

path = "https://postcodes.io/postcodes/"
argument = 'SE172HY'
url = path + argument

resq = requests.get(url)
# print (resq)
# print (resq.status_code)
#print(resq.headers)
# print(resq.content)

#JSON decoder

# print(resq.json())
# print(resq.json().keys())
# print(resq.json()['result'])
# output = resq.json()['result']
# print(output['european_electoral_region'])
# print(output['outcode'])
# print(output['longitude'])
# print(output['latitude'])