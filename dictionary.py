# dictionsary

d={
    "tom":123456,
    "rob":345674,
    "joe":435665,
}
print(d) #{'tom': 123456, 'rob': 345674, 'joe': 435665}
# access element in dictionary
print(d["tom"]) #123456

# add elements
d["sam"]=345678
print(d)

# delete elements from dictionary
del d["sam"] #{'tom': 123456, 'rob': 345674, 'joe': 435665, 'sam': 345678}
print(d) #{'tom': 123456, 'rob': 345674, 'joe': 435665}

# iterate a dict

for key in d:
    print(key,"value:",d[key])
    
for k,v in d.items():
    print(k,v)
    
print("tom" in d) #true

# empty the dict

d.clear()
print(d)
