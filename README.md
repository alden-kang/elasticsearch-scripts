# ElasticSearch Scripts

## What is this?
These are the scripts that are needed to operate the ElasticSearch cluster.

## 구성

### clear_fielddata.py
Use to delete field data caches.
```
python clear_fielddata.py --url test.elastic.co
```

### search_test.py
Use to search performance testing.
```
usage: search_test.py [-h] --url URL [--port PORT] [--threads THREADS]
                      [--requests REQUESTS] --index_name INDEX_NAME

optional arguments:
  -h, --help              show this help message and exit
  --url URL               the url of cluster
  --port PORT             the port of cluster (default 9200)
  --threads THREADS       the number of search threads (default 1)
  --requests REQUESTS     the number of times search request of cluster (default 1)
  --index_name INDEX_NAME the name of index to test

ex) python ./search_test.py --url test.elastic.co --index_name test-index
```
Before you run, modify the query to suit the cluster and test it. The query for the default search test is shown below.
```
"query": {
      "query_string": {
          "query": "*"
      }
  }
```
