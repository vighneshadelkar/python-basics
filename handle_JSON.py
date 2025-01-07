# working with json

book={}

book["tom"]={
    "name":"tom",
    "address":"b1",
    "phone":1234
}
book["bob"]={
    "name":"bob",
    "address":"b1",
    "phone":1234
}
print(book)

import json
# converts dict to string which is then converted to json
s=json.dumps(book)
# converts string in json format to dict
book=json.loads(s)
print(s)
print(type(book))
for person in book:
    print(book[person])
