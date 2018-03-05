#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import traceback

from urllib3 import HTTPConnectionPool

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="the url of cluster (default localhost)", required=True)
parser.add_argument("--port", help="the port of cluster (default 9200)", default=9200, required=False)

args = parser.parse_args()

url = args.url
port = args.port

es_connection_pool = HTTPConnectionPool(url, port=port, maxsize=100)

response = es_connection_pool.request(
            'GET',
            '/_cat/indices?h=i,fielddataMemory&format=json'
)

for fielddata_info in json.loads(response.data) :

    if fielddata_info['fielddataMemory'] != "0b":

        print "[CLEAR CACHE] INDEX NAME : %s, FIELDDATA : %s" % (fielddata_info['i'], fielddata_info['fielddataMemory'])

        response = es_connection_pool.request(
                    'POST',
                    '/%s/_cache/clear' % (fielddata_info['i'])
        )

        print response.data
