# list 

# list is similar to array 
# list is immutable 
# list can have elements of diff data types too

items=[1,2,3,4,1]
print(items)

items[0]=10
print(items)

items[0]="c"
print(items) #['c', 2, 3, 4, 1]

# slicing 
print(items[0:2])

# last element index 1 from the end
print(items[-1])

items.append(100) 
print(items) #['c', 2, 3, 4, 1, 100]

# insert element at a particular location
items.insert(1,212)
print(items) # ['c', 212, 2, 3, 4, 1, 100]

food=["bread","fruits"]
bathroom=["soap","shampoo"]

items=food+bathroom
print(items) #['bread', 'fruits', 'soap', 'shampoo']

#  to find length of list
print(len(items))

print("bread" in items) #true
print("soda" in items) #false
