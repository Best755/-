from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="47.96.129.100", port=9200)
# es.indices.create(index="cggg", ignore=400)
#
# data = {"name": "小明", "age": "8", "gender": "男"}
# res = es.index(index="cggg", doc_type="doc", body=data)
# data={"name":"泰国","add_new":2000,"sum_definite":2000,"sum_suspected":2000,"sum_cure":2000,"sum_die":2000,"date":"2020-07-26"}
# res = es.index(index="nice", doc_type="word", body=data)
query={
  "query":{
    "match": {
      "name": "美国"
    }
  }
}

# query={"query": {
#         "bool": {
#             "must": [
#                 {
#                     "match": {
#                         "name": "泰国",
#                     },
#
#                 },
#                 {
#                     "match": {
#                         "date": "2020-07-23",
#                     },
#
#                 },
#             ]
#         }
#     }
# }
ret = es.search(index='nice', doc_type='word', body=query,size=5)
# print(ret)
s=ret["hits"]["hits"]
for i in s:
    print("-------")
    print(i["_source"])