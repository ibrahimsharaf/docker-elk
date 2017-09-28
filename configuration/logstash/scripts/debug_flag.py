import sys
from elasticsearch import Elasticsearch, exceptions

source_query = ''

for logstash_line in sys.stdin:
    source_query = str(logstash_line).strip()
    with open("/var/test.txt", "w") as text_file:
        text_file.write("Pipe Output was: {}".format(source_query))
    break

# update all documents matching the source and running state
query = {
     "script": {
        "inline": "ctx._source.spider_state='hefna_debug'",
        "lang": "painless"
     },
     "query": {
        "bool": {
          "must": [
            {
              "match" : {
                "spider_state": "test_debug777"
              }
            },
            {
              "match" : {
                "source": "{}".format(source_query)
              }
            }
          ]
        }
     }
}

#print(query)
# fix this host to whatever es is reachable at
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
#es = Elasticsearch()
es.update_by_query(body=query, doc_type='', index='_all')
