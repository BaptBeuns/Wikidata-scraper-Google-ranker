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
output_name = u"" if len(sys.argv)==1 else sys.argv[2]

with io.open(file_name,'r',encoding='utf8') as fileId:
    f = fileId.read()

names = f.split('\n')
names_length = len(names)
toolbar_width = names_length

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

with io.open(output_name,'w',encoding='utf8') as output:
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
                try:
                    name = element['result']['name']
                except KeyError:
                    name = query.split(',')[0]
                try:
                    url = element['result']['detailedDescription']['url']
                except KeyError:
                    url = u"http://google.com/search?q=" + query.split(',')[0]
                output.write(u"%s, %s, <a href='%s'>%s</a>\n" % (query.split(',')[0], score, url, name))
                sys.stdout.write("-")
                sys.stdout.flush()

sys.stdout.write("\n")
