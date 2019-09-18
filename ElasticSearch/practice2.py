# Import Elasticsearch package
from elasticsearch import Elasticsearch
# Connect to the elastic cluster
es=Elasticsearch([{'host':'localhost','port':9200}])
es

e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}

res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)

# Let's insert some more documents
e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}
res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)

print(res['created'])