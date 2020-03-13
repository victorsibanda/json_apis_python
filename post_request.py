# POST's

import requests
import json

#Needs a JSON object / headers and URL
#.dumps() ---> string that is json
# .dump() ----> text file that is json

# filipe = {'name': 'FILIPE PV', 'SuperPower':'Patienece..','prep level':'wine and batteries for the xbox'}
#
# json.dump(filipe,'filejson')
#
#
#

json_body = json.dumps({
"postcodes" : ["OX49 5NU", "M32 0JG", "NE30 1DP"]
})

print(json_body)

header = {'Content-type':'application/json'}
url = "https://postcodes.io/postcodes/"

#Making post API Call with JSON Body, header and URL
resq = requests.post(url,headers=header,data = json_body)

print(resq)







