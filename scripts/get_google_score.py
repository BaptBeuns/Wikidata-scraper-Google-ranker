#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Example of Python client calling Knowledge Graph Search API.
Can be modified for other purposes -> retrieve photo of the person, wikipedia description...
"""
import json
import urllib
import sys
import io

file_name = u"" if len(sys.argv)==1 else sys.argv[1]

with io.open(file_name,'r',encoding='utf8') as fileId:
    f = fileId.read()

names = f.split('\n')

for query in names:
    if query != u'':
        api_key = open('.api_key').read()
        service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

        # Necessary to avoid the unicode errors
        query_name = query.split(',')[0]
        if isinstance(query_name, unicode):
            query_name = query_name.encode('UTF-8')

        params = {
            'query': query_name,
            'limit': 1,
            'indent': True,
            'key': api_key,
            'types': 'Person',
        }
        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        if len(response['itemListElement']) > 0:
            element = response['itemListElement'][0]
            score = str(int(element['resultScore']))
            name = element['result']['name']
            url = element['result']['detailedDescription']['url']
            print(u"%s, %s, <a href='%s'>%s</a>" % (query.split(',')[0], score, url, name))
