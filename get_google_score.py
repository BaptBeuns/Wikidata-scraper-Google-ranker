#!/usr/bin/python
"""
Example of Python client calling Knowledge Graph Search API.
Call by ./google.py 'ARG1' and it will give you the more relevant Person.
Can be modified for other purposes -> retrieve photo of the person, wikipedia description...
"""
import json
import urllib
import sys

api_key = open('.api_key').read()
query = 'Taylor Swift' if len(sys.argv)==1 else sys.argv[1]
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 1,
    'indent': True,
    'key': api_key,
    'types': 'Person',
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
if len(response['itemListElement']) > 0:
  element = response['itemListElement'][0]
  #print element['result']['name'] + ',' + str(element['resultScore'])
  print '%07d' % int(element['resultScore'])
